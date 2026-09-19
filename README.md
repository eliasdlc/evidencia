# evidencia

Host de imagenes para los PR. Los repos de Elias son privados, y GitHub solo
renderiza una imagen dentro del cuerpo de un PR si su URL es publica: por eso
las capturas viven aqui y no en el repo que se esta revisando.

No es un repo de trabajo. No se clona, no se edita a mano, no lleva codigo.

## Que se sube

    <proyecto>/<rama>/<sha7>/<pantalla>@<ancho>x<alto>.png

El `sha7` va en la ruta y nunca se reescribe un archivo existente: el proxy de
imagenes de GitHub (camo) cachea por URL, asi que una captura nueva en una ruta
vieja seguiria mostrando la imagen anterior dentro del PR.

## Que nunca se sube

Todo lo de aqui es publico y queda en el historial de git para siempre.

- Datos reales de una persona, un paciente, un cliente o un negocio.
- La cuenta de Elias en cualquier pantalla. Las capturas salen de cuentas
  semilla de prueba.
- Claves, tokens, URLs firmadas, QR, correos, telefonos, coordenadas de casa.

## Como se sube

    agentes evidencia <proyecto>/<rama>/<sha7> captura.png ...

Imprime el Markdown ya listo para la seccion `## Proof` del PR.
