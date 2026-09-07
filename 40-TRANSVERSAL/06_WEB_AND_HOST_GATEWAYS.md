# Web and Host Gateways

## Principle

Host OS and Web are useful external capability domains. Shaper should cooperate with them through controlled crossings rather than either trusting them completely or trying to replace them.

## Web Surface

The Workspace embeds/opens an existing web engine. It provides the shell, permissions and gateways around it.

Potential engines differ by platform; final selection remains an implementation decision.

### Controlled crossings

- upload file/object;
- download → import;
- clipboard Shaper→Web;
- clipboard Web→Shaper;
- microphone/camera;
- passkey/authentication;
- print;
- screen share;
- external navigation.

Each can be policy-controlled.

## Browser state

Deployment policy may choose:

- disposable sessions;
- persistent sessions by approved domain;
- isolated profiles per organization/context;
- no third-party extensions;
- download quarantine/import scanning.

## Web Agent

Agents may use web search/fetch/automation separately from the visible Web Surface. Visible intervention is used when a human needs to inspect, authenticate or take over.

## Host file picker

Default file access is bounded by a user selection or explicit managed location. The client should not require permanent access to the entire home directory merely to import documents.

## External native application

```text
Shaper object
→ authorize export
→ temporary controlled materialization
→ native app
→ save/watch/close
→ re-import as new version
→ cleanup temporary material
```

Define what happens if the app crashes, the file is saved elsewhere, or the user abandons the flow.

## Device Gateway

Use host drivers/APIs for:

- printer;
- scanner;
- audio;
- camera;
- barcode;
- smart card;
- USB/serial devices.

Shaper policy decides which requests are allowed; the Host OS remains the hardware abstraction layer.

## Success criterion

The organization gains access to the full external ecosystem without turning the external ecosystem into an implicit trusted member of the Shaper universe.
