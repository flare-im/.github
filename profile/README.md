<p align="center">
  <img src="./assets/flare-im-system-map.svg" alt="Flare IM protocol weave" width="100%" />
</p>

<h1 align="center">flare.im</h1>

<p align="center">
  <strong>One realtime core. Native SDK surfaces. Product rules stay above the wire.</strong><br />
  业务中立的即时通讯基础设施: Rust 单核心、七端 SDK、跨端 UI Kit、可组合社交业务层。
</p>

<p align="center">
  <a href="https://github.com/flare-im/flare-im-core-server">Core server</a>
  ·
  <a href="https://github.com/flare-im/flare-im-core-sdk">Rust client engine</a>
  ·
  <a href="https://github.com/flare-im/flare-im-core-client-sdk">Client SDKs</a>
  ·
  <a href="https://github.com/flare-im/flare-im-design">UI kit</a>
</p>

## The Shape Of The System

Flare IM is a full-stack instant messaging platform for teams that need the realtime layer to stay clean, inspectable, and portable. The core carries messaging behavior; platform packages adapt it; product features stay above it.

That boundary is the point of the project.

| Boundary | What Lives There | Public Entry Point |
| --- | --- | --- |
| Wire | QUIC/WebSocket transport, connection foundations, service discovery | [flare-core](https://github.com/flare-im/flare-core) |
| Contract | DDD/CQRS protocol contracts and generated surfaces | [flare-proto](https://github.com/flare-im/flare-proto), [flare-grpc-proto](https://github.com/flare-im/flare-grpc-proto) |
| Server | Messaging, session, sync, storage, media, delivery, and fanout services | [flare-im-core-server](https://github.com/flare-im/flare-im-core-server) |
| Client core | Reliable send, sync convergence, ordering, local state, native/web runtime behavior | [flare-im-core-sdk](https://github.com/flare-im/flare-im-core-sdk) |
| SDK surface | TypeScript, Swift, Kotlin, Dart, Flutter, HarmonyOS, and example app packages | [flare-im-core-client-sdk](https://github.com/flare-im/flare-im-core-client-sdk) |
| Experience | Cross-platform IM components, shared tokens, and native UI implementations | [flare-im-design](https://github.com/flare-im/flare-im-design) |

## Start By Intent

| If You Want To... | Start Here |
| --- | --- |
| Inspect the realtime server path | [flare-im-core-server](https://github.com/flare-im/flare-im-core-server) |
| Build against the client SDK contract | [flare-im-core-client-sdk](https://github.com/flare-im/flare-im-core-client-sdk) |
| Understand the Rust client engine | [flare-im-core-sdk](https://github.com/flare-im/flare-im-core-sdk) |
| Reuse the interface language | [flare-im-design](https://github.com/flare-im/flare-im-design) |
| Try a web reference app | [flare-core-web-demo](https://github.com/flare-im/flare-core-web-demo) |
| Try desktop with Tauri | [flare-core-tauri-demo](https://github.com/flare-im/flare-core-tauri-demo) |
| Try mobile foundations | [flare-core-ios-demo](https://github.com/flare-im/flare-core-ios-demo), [flare-core-android-demo](https://github.com/flare-im/flare-core-android-demo), [flare-core-flutter-demo](https://github.com/flare-im/flare-core-flutter-demo) |

## Engineering Principles

- **Neutral core**: IM infrastructure stays independent from social, community, or enterprise product policy.
- **One behavior source**: shared realtime behavior belongs in the Rust client engine, not in every platform app.
- **Typed contracts first**: protocol and SDK surfaces use explicit fields, enums, and generated contracts.
- **Production paths only**: pre-release work favors one clean implementation path over compatibility shims.
- **Measured realtime quality**: latency, ordering, backpressure, retry, and sync recovery are first-class design concerns.

## Status

Flare IM is under active pre-release development. Public repositories are opened as contracts, SDKs, and examples become stable enough for outside inspection.
