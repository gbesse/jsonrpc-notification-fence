# jsonrpc-notification-fence

## Français

Séparer notifications et appels JSON-RPC sur un vrai flux.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m jsonrpc_notification_fence examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Un vrai processus pair stdio reçoit les messages ; seules les requêtes avec id obtiennent une réponse. Expose le comptage naïf erroné et les id null ambigus.

### Limites

Pair fixe echo/method-not-found, sans serveur MCP ni transport réseau ; pas implémentation JSON-RPC complète. Identifiants doublés signalés, pas résolus.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Separate JSON-RPC notifications and calls on an actual stream.

Synthetic data; no network access or secret required.

```sh
python -m jsonrpc_notification_fence examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

An actual stdio peer process receives messages; only requests with id receive replies. Exposes incorrect naive counting and discouraged null IDs.

### Limits

Fixed echo/method-not-found peer, no MCP server or network transport; not a complete JSON-RPC implementation. Duplicate IDs reported, not resolved.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Separar notificaciones y llamadas JSON-RPC en un flujo real.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m jsonrpc_notification_fence examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Un proceso par stdio real recibe mensajes; solo solicitudes con id reciben respuesta. Expone conteo ingenuo incorrecto e identificadores null desaconsejados.

### Límites

Par fijo echo/method-not-found, sin servidor MCP ni red; no implementación JSON-RPC completa. Identificadores duplicados señalados, no resueltos.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.jsonrpc.org/specification
