<p align="center">
  <img src="./assets/flare-im-system-map.svg" alt="Flare IM system map" width="100%" />
</p>

<h1 align="center">flare.im</h1>

<p align="center">
  Business-neutral realtime messaging infrastructure built around a Rust core, multi-platform SDKs, and a consistent cross-platform IM experience.
</p>

<p align="center">
  <a href="https://github.com/flare-im/flare-im-core-server"><img alt="Core server" src="https://img.shields.io/badge/core%20server-Rust-dea584?style=flat-square&logo=rust&logoColor=white"></a>
  <a href="https://github.com/flare-im/flare-im-core-client-sdk"><img alt="Client SDKs" src="https://img.shields.io/badge/client%20SDKs-7%20platforms-1f6feb?style=flat-square"></a>
  <a href="https://github.com/flare-im/flare-im-design"><img alt="UI kit" src="https://img.shields.io/badge/UI%20Kit-cross--platform-7c3aed?style=flat-square"></a>
  <img alt="Stage" src="https://img.shields.io/badge/stage-pre--release-2da44e?style=flat-square">
</p>

<p align="center">
  English | <strong>中文</strong>
</p>

## What We Are Building

Flare IM is a full-stack instant messaging platform for teams that need a clear boundary between infrastructure, product rules, and user experience.

Flare IM 是一套全栈即时通讯基础设施: Rust 单核心、七端客户端 SDK、跨端 UI Kit, 以及可组合的社交业务层。

Our current focus:

- Keep the IM core business-neutral, so product rules stay above the infrastructure layer.
- Move shared client behavior into the Rust core, including send reliability, sync convergence, ordering, and local state.
- Keep platform packages native-feeling while preserving one canonical contract.
- Provide reference apps and UI foundations that make real integration work easier to inspect.

## Public Repository Map

| Area | Repository | Purpose |
| --- | --- | --- |
| Transport | [flare-core](https://github.com/flare-im/flare-core) | QUIC/WebSocket transport, connection management, service discovery foundations. |
| Contracts | [flare-proto](https://github.com/flare-im/flare-proto) | Core protobuf contracts. |
| Contracts | [flare-grpc-proto](https://github.com/flare-im/flare-grpc-proto) | gRPC-oriented protocol contracts. |
| Server | [flare-im-core-server](https://github.com/flare-im/flare-im-core-server) | Core server services for messaging, sessions, sync, storage, media, and delivery paths. |
| Client Core | [flare-im-core-sdk](https://github.com/flare-im/flare-im-core-sdk) | Rust client engine for native and web runtimes. |
| Client SDKs | [flare-im-core-client-sdk](https://github.com/flare-im/flare-im-core-client-sdk) | TypeScript, Swift, Kotlin, Dart, Flutter, HarmonyOS, and example app packages. |
| Design | [flare-im-design](https://github.com/flare-im/flare-im-design) | Cross-platform IM UI kit with shared tokens and native implementations. |
| Examples | [flare-core-web-demo](https://github.com/flare-im/flare-core-web-demo) | Web demo app for the core client experience. |
| Examples | [flare-core-tauri-demo](https://github.com/flare-im/flare-core-tauri-demo) | Desktop demo app built with Tauri. |
| Examples | [flare-core-flutter-demo](https://github.com/flare-im/flare-core-flutter-demo) | Flutter demo app for mobile and desktop exploration. |
| Examples | [flare-core-ios-demo](https://github.com/flare-im/flare-core-ios-demo) | iOS demo app. |
| Examples | [flare-core-android-demo](https://github.com/flare-im/flare-core-android-demo) | Android demo app. |

## Architecture Principles

- **Neutral core**: IM infrastructure stays independent from social, community, or enterprise product policy.
- **One behavior source**: shared realtime behavior belongs in the core client engine, not in every platform app.
- **Typed contracts first**: protocol and SDK surfaces use explicit fields, enums, and generated contracts.
- **Production paths only**: pre-release work favors one clean implementation path over compatibility shims.
- **Measured realtime quality**: latency, ordering, backpressure, retry, and sync recovery are first-class design concerns.

## Start Here

- Server foundation: [flare-im-core-server](https://github.com/flare-im/flare-im-core-server)
- Client SDK surface: [flare-im-core-client-sdk](https://github.com/flare-im/flare-im-core-client-sdk)
- Cross-platform UI: [flare-im-design](https://github.com/flare-im/flare-im-design)
- Web reference app: [flare-core-web-demo](https://github.com/flare-im/flare-core-web-demo)

## Status

Flare IM is under active pre-release development. Public repositories are opened as the contracts, SDKs, and examples become stable enough for outside inspection.
