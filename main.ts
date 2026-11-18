// Entry for make.fun news-image-20261117: "Sum up 17 November's world news
// in one image". The image is a 1024x1024 PNG newspaper front page summing
// up Tuesday 17 November 2026 — the Kerch Bridge strike, Trump in Manila,
// Iran's drones at a US radar site in Bahrain, Japan scrambling jets,
// UK sanctions on settlement builders, and Nvidia's earnings — composed
// in this session from a generated text-free illustration plus crisp
// PIL-rendered text. Node 22, standard library only, no network.
// The program copies the image to the output directory; run it with:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? './out';
mkdirSync(outDir, { recursive: true });
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
