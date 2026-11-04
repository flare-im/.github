<p align="center">
  <img src="./assets/flare-im-logo-mark.svg" alt="Flare IM logo mark" width="68" />
</p>

<h1 align="center">flare.im</h1>

<p align="center">English · <a href="https://github.com/flare-im/.github/blob/main/profile/README.zh-CN.md">Simplified Chinese</a></p>

<p align="center">
  <strong>Realtime messaging infrastructure with one Rust behavior core and native SDK surfaces.</strong><br />
  Server microservices, SDKs for seven platforms, and a cross-platform UI kit.
</p>

<p align="center">
  <img src="./assets/flare-im-system-map.svg" alt="Flare IM protocol weave" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/flare-im/flare-transport">Transport</a>
  ·
  <a href="https://github.com/flare-im/flare-core-server">Server</a>
  ·
  <a href="https://github.com/flare-im/flare-core-sdk-engine">Client core</a>
  ·
  <a href="https://github.com/flare-im/flare-core-sdk">SDKs</a>
  ·
  <a href="https://github.com/flare-im/flare-im-design">Design</a>
</p>

## Start Building

- **Core messaging** — [Start the public server and run a message smoke check](https://github.com/flare-im/flare-core-server#flare-im-core) or [browse the reference apps](https://github.com/flare-im/flare-core-examples).
- **Plugin development** — [Build your first gRPC or WASM plugin](https://github.com/flare-im/flare-plugin-devkit), starting with the [Echo example](https://github.com/flare-im/flare-plugin-devkit/blob/main/flare-plugin-host/examples/echo_plugin.rs). See the [public catalog](https://github.com/flare-im/flare-plugin-catalog) for metadata.
- **Pinned Core sources** — [Source baseline and checkout instructions](https://github.com/flare-im/.github/blob/main/baselines/README.md).

Core, the UI kit, and plugin development tools are open source. Flare Social and first-party commercial plugin implementations are maintained separately.

## Organization Focus

Flare IM is building a reusable instant messaging stack where the realtime behavior is implemented once, tested close to the core, and exposed through platform-native SDKs. Product-specific social features, plugin capabilities, and app choices live above the core instead of leaking into transport or protocol contracts.

The current project is organized around a few firm boundaries:

- **Transport stays reusable**: connection management, QUIC/WebSocket paths, and service discovery live below product semantics.
- **Contracts are explicit**: proto, bindings, and SDK specs define typed boundaries before platform packages adapt them.
- **Client behavior is shared**: send reliability, sync recovery, ordering, storage policy, and lifecycle behavior belong in the Rust client engine.
- **UI remains portable**: design tokens and IM components give the example apps a consistent interface language without making UI rules part of the core.
- **Business layers compose on top**: social, community, enterprise, and plugin features stay outside the business-neutral IM foundation.

## System Map

| Layer | Public Repository | Responsibility |
| --- | --- | --- |
| Wire | [flare-transport](https://github.com/flare-im/flare-transport) | Transport foundations for QUIC/WebSocket connections and service discovery. |
| Contract | [flare-protocol](https://github.com/flare-im/flare-protocol), [flare-protocol-grpc](https://github.com/flare-im/flare-protocol-grpc) | Protocol contracts for DDD/CQRS services and generated integration surfaces. |
| Server | [flare-core-server](https://github.com/flare-im/flare-core-server) | Messaging, session, sync, storage, media, delivery, and fanout services. |
| Server runtime | [flare-server-runtime](https://github.com/flare-im/flare-server-runtime) | Shared server infrastructure used by the Core services. |
| Client core | [flare-core-sdk-engine](https://github.com/flare-im/flare-core-sdk-engine) | Rust client engine for reliable send, sync convergence, ordering, and local state. |
| SDK surface | [flare-core-sdk](https://github.com/flare-im/flare-core-sdk) | TypeScript, Swift, Kotlin, Dart, Flutter, and HarmonyOS packages. |
| Experience | [flare-im-design](https://github.com/flare-im/flare-im-design) | Cross-platform IM UI kit, shared tokens, and native component implementations. |

## Start By Intent

| If You Want To... | Start Here |
| --- | --- |
| Inspect the realtime server path | [flare-core-server](https://github.com/flare-im/flare-core-server) |
| Build against the client SDK contract | [flare-core-sdk](https://github.com/flare-im/flare-core-sdk) |
| Understand the Rust client engine | [flare-core-sdk-engine](https://github.com/flare-im/flare-core-sdk-engine) |
| Reuse the interface language | [flare-im-design](https://github.com/flare-im/flare-im-design) |
| Try a web reference app | [Web example](https://github.com/flare-im/flare-core-examples/tree/main/apps/flare-core-web-app) |
| Try desktop with Tauri | [Tauri example](https://github.com/flare-im/flare-core-examples/tree/main/apps/flare-core-tauri-app) |
| Try mobile foundations | [iOS](https://github.com/flare-im/flare-core-examples/tree/main/apps/flare-core-ios-app), [Android](https://github.com/flare-im/flare-core-examples/tree/main/apps/flare-core-android-app), [Flutter](https://github.com/flare-im/flare-core-examples/tree/main/apps/flare-core-flutter-app) |
| Develop a Flare plugin | [Flare Plugin DevKit](https://github.com/flare-im/flare-plugin-devkit) |
| Browse plugin metadata | [Flare Plugin Catalog](https://github.com/flare-im/flare-plugin-catalog) |

## Engineering Principles

- **Neutral core**: IM infrastructure stays independent from social, community, or enterprise product policy.
- **One behavior source**: shared realtime behavior belongs in the Rust client engine, not in every platform app.
- **Narrow waist**: generated SDK surfaces cross a small, stable runtime boundary instead of duplicating platform logic.
- **Typed contracts first**: protocol and SDK surfaces use explicit fields, enums, and generated contracts.
- **Production paths only**: pre-release work favors one clean implementation path over compatibility shims.
- **Measured realtime quality**: latency, ordering, backpressure, retry, and sync recovery are first-class design concerns.

## Status

Flare IM is under active pre-release development. Public repositories are opened as contracts, SDKs, and examples become stable enough for outside inspection.
