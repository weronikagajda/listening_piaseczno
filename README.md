# Piaseczno: listening (map 4.3.3-A2)

A phone page in the same visual language as the website. It reads your GPS position, puts you in the model, and plays the sound of the four planned halls at the level the website's noise model gives for where you stand. Everything runs on the phone. Your position is sent nowhere.

## Put it online (needed for GPS)

Location only works on a page served over **https**. It doesn't work in the claude.ai preview or from a file opened on the phone. Two quick ways:

- **Netlify Drop**: go to app.netlify.com/drop and drag this folder onto the page. You get an https address at once. A free account keeps the site.
- **GitHub Pages**: make a private or public repository, upload this folder, then turn on Settings → Pages.

The page carries `noindex`, so search engines skip it. The address is still public to anyone who has it.

## Before the walk

1. Open the address on your phone and press **Start**. Allow location when asked.
2. With headphones, open **Settings** and play the **40 dB reference**. Set the phone's volume so it sounds as loud as a quiet street at night, then leave the volume there.
3. **Measure the street** uses the phone's microphone. Compare it once with a sound level meter or the sensor, then set the offset in Settings. Treat the values as indicative.
4. **Try it from afar** lets you drag yourself through the street from anywhere, which is useful for testing in Leuven.

## Recordings

- **On the spot:** in Settings, use **Add a recording from this phone** (m4a, mp3 or wav). Keep loops to 1–2 min so they stay light on the phone.
- **Shipped with the page:** put the files in `sounds/` and list them in `sounds.json` next to `build.py`, then rebuild:

```json
[{"src":"sounds/data4_fence_night.m4a","label":"DATA4 Jawczyce, fence, night","place":"Przyparkowa","date":"2026-11-13","dB":52}]
```

The recording gives the character of the sound. The model still sets its level where you stand. Each file is matched to the hum's loudness. The measured `dB` is kept with it, to compare with the model.

## The walk log

While Start is on, each position is kept on the phone with the modelled level and, if measuring, the street level. **Export GPX / CSV** saves it for QGIS (Settings). It shows where you walked, including near home, so keep it private.

## What the numbers are

- **Level:** the website's model, the sum over the four halls of 75.5 − 20·log10(max(distance to hall, 12) + 25), fitted to the noise report's 25 values (about 1.3 dB).
- **"Inside / beyond the 40 dB line":** read from the line the report itself draws, as traced. Along that line the model gives 33–43 dB, so the number and the line can disagree by a few dB.
- **Okulickiego:** drawn but silent, because it has no published layout.
- **Not in the model:** generators, low frequency and the screens.
- **Positions:** GPS (WGS84) is converted to EPSG:2180, which is exact, and then to the website's model frame (x = E − 639266, y = N − 471094). The halls and the 40 dB line are in true EPSG:2180. Buildings and OpenStreetMap features may be off by about 5–10 m.

## Rebuild

The source is in `source/`: `tpl.html`, `build.py` and `sounds.json`. Unzip claude_working_files_2026-11-08.zip, then put these three files in a new folder `listen/` next to `site/`, put three.js r128 at `three_pkg/package/build/three.min.js` (`npm pack three@0.128.0`), then run `python3 build.py`. That writes `out/index.html`.
