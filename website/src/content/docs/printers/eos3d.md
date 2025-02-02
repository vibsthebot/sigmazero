---
title: "EOS 3D"
description: "A cheap cantilever 3D printer with full self calibration capabilities."
project_name: "EOS 3D"
repository: "https://raw.githubusercontent.com/AdamTuraj/EOS-3D/refs/heads/main/JOURNAL.md"
---
<center><h1>EOS 3D</h1></center>

**This document tracks progress for the YSWS portion of this project. It also serves as a journal documenting the development process.**

## Preface

Before starting this project, I must outline the key requirements to ensure clear project direction and successful execution. I initially came up with the following requirements:

- $300 (USD) budget
- Klipper compatibility
- No calibration printing is required
- 180x180mm build space
- Cantilever structure
- CFD-optimized part cooling
- Safety considerations:
  - Must not pose a fire hazard
  - Must not cause harm to the user
- [PicoMMU](https://github.com/lhndo/LH-Stinger/tree/main/User_Mods/MMU/Stinger%20Pico%20MMU%20-%20%40LH) compatibility

Although I have extensive experience working with 3D printers, this is my first time designing one. Through this process, I aim to deepen my understanding of 3D printer mechanics, refine my CAD skills, and improve my approach to mechanical design. Additionally, thanks to Hack Club, this project offers the added benefit of a free printer.

The name of this project, **EOS 3D**, is inspired by the Greek goddess of dawn, Eos. Dawn symbolizes new beginnings, reflecting a personal milestone in my projects and an entry point for tinkerers.

## Day 1 (February 1st, 2025)

Hours worked: **8**

Total hours on project: **8**

### BOM Selection

Creating the **Bill of Materials (BOM)** required balancing cost-effectiveness with performance and safety. While selecting parts, I took into account the following:

- A budget hotend from a reputable brand to ensure safety and good flow.
- A reliable direct-drive extruder.
- The **Cartographer probe** for its high-resolution bed meshing capabilities and automatic Z-offset calibration via Carto Survey.
- BTT SKR Mini and a Raspberry PI for its cost-effective control.
- A cheap heated bed with a PEI spring steel sheet.
- A PSU with a large overhead from a reputable brand.

Compiling and refining the BOM took approximately **four hours**.

**[BOM Link](https://docs.google.com/spreadsheets/d/1bcc6GYku32MK7iQRG4SbK_M0EsOTyS6UKOEk-3bwc5s)**

### Toolhead Development

With the BOM completed, I decided to tackle the printer's tool head first, as it serves as an "anchor point" for the build.

I began by modelling the X-axis rods and bearings to establish clearance constraints between the toolhead and the rods.

Next, I imported the CAD models for the Sherpa Mini extruder and the E3D V6 hotend, then started designing a mounting solution. I opted for a clamping mechanism for the hotend, as shown in the image below:

![Hotend clamping mechanism](https://cloud-6ea58jaj9-hack-club-bot.vercel.app/0image.png)

By the end of the day, I refined the mounting system and securely integrated the Sherpa Mini with the mount. Below is the final design on day 1 (ignore the mesh issues on the Sherpa; those were present in the CAD model):

![Day 1 image update](https://cloud-56t3p8blt-hack-club-bot.vercel.app/0image.png)
