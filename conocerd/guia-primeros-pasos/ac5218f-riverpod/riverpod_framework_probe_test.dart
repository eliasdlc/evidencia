import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

class Counter extends Notifier<int> {
  @override
  int build() => 0;
  void increment() => state++;
}
final counter = NotifierProvider<Counter, int>(Counter.new);
final fetched = FutureProvider<int>((ref) => ref.watch(counter));
final derived = FutureProvider<int>((ref) async => await ref.watch(fetched.future));

void main() {
  testWidgets('paused async dependency refresh resumes without a build error', (tester) async {
    final visible = ValueNotifier(true);
    final container = ProviderContainer();
    addTearDown(visible.dispose);
    addTearDown(container.dispose);
    await tester.pumpWidget(UncontrolledProviderScope(
      container: container,
      child: MaterialApp(home: ValueListenableBuilder<bool>(
        valueListenable: visible,
        builder: (_, enabled, _) => TickerMode(
          enabled: enabled,
          child: Consumer(builder: (_, ref, _) => Text('${ref.watch(derived).value}')),
        ),
      )),
    ));
    await tester.pumpAndSettle();
    visible.value = false;
    await tester.pump();
    container.read(counter.notifier).increment();
    await tester.pump();
    visible.value = true;
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
    expect(find.text('1'), findsOneWidget);
  });
}
