# Flare Core source baselines

A source baseline pins exact revisions for the public Core server and SDK, including the design kit used by client integrations. The baseline describes sources. Built artifacts, signatures, compatibility promises and deployment acceptance are recorded separately by a release.

## Check out the pinned sources

Run these commands from a local clone of this repository. Use Python 3 and Git, and choose a new destination directory.

```sh
python3 baselines/checkout.py baselines/core-source-2026-11-03.json ./core-baseline
```

The script checks out the exact commits over public HTTPS without using your Git credentials. It stops on a missing revision, without falling back to a branch. If the network fails, choose a fresh destination for the retry. Follow the [Core server instructions](https://github.com/flare-im/flare-core-server#flare-im-core) for runtime requirements and the message smoke check.

The [reference apps](https://github.com/flare-im/flare-core-examples) and [Plugin DevKit](https://github.com/flare-im/flare-plugin-devkit) have separate lifecycle and compatibility checks. Their revisions are outside this server and SDK baseline.

Add a new manifest when promoting a new source baseline. Keep existing manifests available so a maintainer can retrieve the same source revisions later.
