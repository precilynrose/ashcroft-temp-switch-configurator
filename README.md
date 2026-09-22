# Ashcroft T4/T7 Temperature Switch Configurator

A buyer-friendly, self-contained product configurator for Ashcroft's T4 (NEMA 4X watertight) and T7 (NEMA 7/9 explosion-proof) temperature switches, built as a demo by [swiftyquote.com](https://www.swiftyquote.com).

- **Open it:** double-click [`ashcroft-temperature-switch-configurator.html`](ashcroft-temperature-switch-configurator.html) — no server or internet connection needed. Logo, product photos and the PDF library are all inlined.
- **Source:** [`src/template.html`](src/template.html) is the editable template (placeholders `__LOGO__`, `__T4__`, `__T7__`, `__JSPDF__`). Run `python3 src/build.py` to rebuild the standalone file after editing it.
- **Assets:** `src/assets/` holds the logo and product photos extracted from Ashcroft's published data sheet; `src/jspdf.umd.min.js` is the vendored jsPDF library used to generate the downloadable spec sheet in-browser.

## What it does

A 7-step wizard (Application → Conditions → Installation → Range → Switch → Options → Review) walks a non-technical buyer through the real options on Ashcroft's T4/T7 data sheet, validates their answers against the data sheet's limits (temperature range, ambient rating, load current, etc.), and produces:

- **A downloadable PDF** spec sheet summarizing the configuration, generated client-side with jsPDF.
- **A quotation request** — a modal that opens a pre-filled email (CC'd and subject-tagged for tracking) or posts to a configurable form endpoint.

All settings (recipient email, CC, tracking tag, form endpoint, company info) are in a `SETTINGS` block near the top of the script.

## Data source

Content is drawn from Ashcroft's published data sheet (`t4-t7_switch_ds_RevI_10-18-23`) and product pages at ashcroft.com. This is an unofficial, third-party demo — not an Ashcroft product. All data, photos and trademarks belong to Ashcroft Inc. and are used for demonstration purposes only.
