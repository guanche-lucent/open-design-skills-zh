# 署名与许可文件核查

日期：2026-10-13。逐项检查 163 个目录条目的本地许可文件与 NOTICE 名称记录；这是文件覆盖核查，不是逐项上游授权确认或法律合规认证。

## 发布载体

- 完整仓库：保留上游技能文件、根 LICENSE、NOTICE 与技能自带许可证。
- 精选 ZIP：核查下文列出的文件；本轮不替换现有发布包。
- 在线案例：东京目录附 Three.js MIT 全文、模型署名；新增统一来源与贡献说明入口。

## 待核实项

有 57 项完整内容目录没有单独的许可文件。这不直接等于无授权，可能受根许可证覆盖；需要结合具体上游路径、版本和文件版权声明确认。

这些条目：`agent-browser`, `article-magazine`, `doc-kami-parchment`, `release-notes-one-pager`, `resume-modern`, `faq-page`, `login-flow`, `impeccable-design-polish`, `card-twitter`, `card-xiaohongshu`, `poster-hero`, `social-reddit-card`, `social-spotify-card`, `social-x-post-card`, `data-report`, `research-decision-room`, `gsap-core`, `gsap-frameworks`, `gsap-performance`, `gsap-plugins`, `gsap-react`, `gsap-scrolltrigger`, `gsap-timeline`, `gsap-utils`, `mockup-device-3d`, `design-brief`, `reference-design-contract`, `ecommerce-image-workflow`, `frame-data-chart-nyt`, `frame-flowchart-sticky`, `frame-glitch-title`, `frame-light-leak-cinema`, `frame-liquid-bg-hero`, `frame-logo-outro`, `frame-macos-notification`, `vfx-text-cursor`, `video-hyperframes`, `deck-guizang-editorial`, `deck-open-slide-canvas`, `deck-swiss-international`, `ppt-keynote`, `8-bit-orbit-video-template`, `after-hours-editorial-template`, `swiss-user-research-video-template`, `weread-year-in-review-video-template`, `digits-fintech-swiss-template`, `editorial-burgundy-principles-template`, `html-ppt-retro-quarterly-review`, `swiss-creative-mode-template`, `field-notes-editorial-template`, `chat-motion-overlay`, `export-download-debugging`, `pptx-html-fidelity-audit`, `pr-feedback-quality-gate`, `library-curator`, `od-next-media-inputs`, `brand-extract`

其余条目即使带有 LICENSE，也未在本轮逐一核实字体、图片、示例和依赖是否全部受其覆盖。原 LICENSE-AUDIT.md 是原整理包的历史判断，不能替代本轮验证。

## 逐项记录

| 条目 | 内容形态 | 原包声明许可 | 本地许可文件数 | NOTICE 中包含 ID |
|---|---|---|---:|---|
| `agent-browser` | bundled_content | Apache-2.0 | 0 | 是 |
| `output-skill` | bundled_content | MIT | 1 | 是 |
| `article-magazine` | bundled_content | Apache-2.0 | 0 | 是 |
| `doc` | external_link | unknown | 0 | 是 |
| `doc-kami-parchment` | bundled_content | Apache-2.0 | 0 | 是 |
| `docx` | external_link | Proprietary (© Anthropic, all rights reserved) | 0 | 是 |
| `minimax-docx` | stub | MIT | 0 | 是 |
| `minimax-pdf` | stub | MIT | 0 | 是 |
| `pdf` | external_link | Proprietary (© Anthropic, all rights reserved) | 0 | 是 |
| `release-notes-one-pager` | bundled_content | Apache-2.0 | 0 | 是 |
| `resume-modern` | bundled_content | Apache-2.0 | 0 | 是 |
| `writing-guidelines` | bundled_content | MIT | 1 | 是 |
| `artifacts-builder` | external_link | unknown | 0 | 是 |
| `faq-page` | bundled_content | Apache-2.0 | 0 | 是 |
| `frontend-design` | bundled_content | Apache-2.0 | 1 | 是 |
| `frontend-dev` | stub | MIT | 0 | 是 |
| `login-flow` | bundled_content | Apache-2.0 | 0 | 是 |
| `web-artifacts-builder` | stub | Apache-2.0 | 0 | 是 |
| `brutalist-skill` | bundled_content | MIT | 1 | 是 |
| `emil-design-eng` | bundled_content | MIT | 1 | 是 |
| `gpt-tasteskill` | bundled_content | MIT | 1 | 是 |
| `impeccable-design-polish` | bundled_content | Apache-2.0 | 0 | 是 |
| `minimalist-skill` | bundled_content | MIT | 1 | 是 |
| `soft-skill` | bundled_content | MIT | 1 | 是 |
| `taste-skill` | bundled_content | MIT | 1 | 是 |
| `taste-skill-v1` | bundled_content | MIT | 1 | 是 |
| `card-twitter` | bundled_content | Apache-2.0 | 0 | 是 |
| `card-xiaohongshu` | bundled_content | Apache-2.0 | 0 | 是 |
| `poster-hero` | bundled_content | Apache-2.0 | 0 | 是 |
| `social-reddit-card` | bundled_content | Apache-2.0 | 0 | 是 |
| `social-spotify-card` | bundled_content | Apache-2.0 | 0 | 是 |
| `social-x-post-card` | bundled_content | Apache-2.0 | 0 | 是 |
| `d3-visualization` | stub | MIT | 0 | 是 |
| `data-report` | bundled_content | Apache-2.0 | 0 | 是 |
| `hand-drawn-diagrams` | stub | MIT | 0 | 是 |
| `research-decision-room` | bundled_content | Apache-2.0 | 0 | 是 |
| `emilkowalski-motion` | external_link | unknown | 0 | 是 |
| `flutter-animating-apps` | stub | BSD-3-Clause | 0 | 是 |
| `gsap-core` | bundled_content | MIT | 0 | 是 |
| `gsap-frameworks` | bundled_content | MIT | 0 | 是 |
| `gsap-performance` | bundled_content | MIT | 0 | 是 |
| `gsap-plugins` | bundled_content | MIT | 0 | 是 |
| `gsap-react` | bundled_content | MIT | 0 | 是 |
| `gsap-scrolltrigger` | bundled_content | MIT | 0 | 是 |
| `gsap-timeline` | bundled_content | MIT | 0 | 是 |
| `gsap-utils` | bundled_content | MIT | 0 | 是 |
| `review-animations` | bundled_content | MIT | 1 | 是 |
| `shader-dev` | stub | MIT | 0 | 是 |
| `threejs` | external_link | unknown | 0 | 是 |
| `image-to-code-skill` | bundled_content | MIT | 1 | 是 |
| `redesign-skill` | bundled_content | MIT | 1 | 是 |
| `web-clone` | bundled_content | MIT | 1 | 是 |
| `mockup-device-3d` | bundled_content | Apache-2.0 | 0 | 是 |
| `ad-creative` | stub | MIT | 0 | 是 |
| `competitive-ads-extractor` | external_link | unknown | 0 | 是 |
| `copywriting` | stub | MIT | 0 | 是 |
| `domain-name-brainstormer` | external_link | unknown | 0 | 是 |
| `marketing-psychology` | stub | MIT | 0 | 是 |
| `paywall-upgrade-cro` | stub | MIT | 0 | 是 |
| `apple-hig` | stub | MIT | 0 | 是 |
| `brand-guidelines` | stub | Apache-2.0 | 0 | 是 |
| `color-expert` | stub | CC-BY-4.0 | 0 | 是 |
| `platform-design` | stub | MIT | 0 | 是 |
| `shadcn-ui` | external_link | unknown | 0 | 是 |
| `swiftui-design` | stub | MIT | 0 | 是 |
| `theme-factory` | stub | Apache-2.0 | 0 | 是 |
| `ui-skills` | stub | MIT | 0 | 是 |
| `ui-ux-pro-max` | stub | MIT | 0 | 是 |
| `web-design-guidelines` | bundled_content | MIT | 1 | 是 |
| `wpds` | external_link | unknown | 0 | 是 |
| `brainstorming` | stub | MIT | 0 | 是 |
| `creative-director` | stub | CC-BY-4.0 | 0 | 是 |
| `design-consultation` | stub | MIT | 0 | 是 |
| `design-review` | stub | MIT | 0 | 是 |
| `frontend-skill` | external_link | unknown | 0 | 是 |
| `plan-design-review` | stub | MIT | 0 | 是 |
| `design-brief` | bundled_content | Apache-2.0 | 0 | 是 |
| `design-md` | external_link | unknown | 0 | 是 |
| `enhance-prompt` | external_link | unknown | 0 | 是 |
| `reference-design-contract` | bundled_content | Apache-2.0 | 0 | 是 |
| `stitch-loop` | external_link | unknown | 0 | 是 |
| `stitch-skill` | bundled_content | MIT | 1 | 是 |
| `figma-code-connect-components` | external_link | unknown | 0 | 是 |
| `figma-create-design-system-rules` | external_link | unknown | 0 | 是 |
| `figma-create-new-file` | external_link | unknown | 0 | 是 |
| `figma-generate-design` | external_link | unknown | 0 | 是 |
| `figma-generate-library` | external_link | unknown | 0 | 是 |
| `figma-implement-design` | external_link | unknown | 0 | 是 |
| `figma-use` | external_link | unknown | 0 | 是 |
| `algorithmic-art` | stub | Apache-2.0 | 0 | 是 |
| `canvas-design` | stub | Apache-2.0 | 0 | 是 |
| `hatch-pet` | bundled_content | Apache-2.0 | 1 | 是 |
| `slack-gif-creator` | stub | Apache-2.0 | 0 | 是 |
| `brandkit` | bundled_content | MIT | 1 | 是 |
| `ecommerce-image-workflow` | bundled_content | Apache-2.0 | 0 | 是 |
| `imagegen-frontend-mobile` | bundled_content | MIT | 1 | 是 |
| `imagegen-frontend-web` | bundled_content | MIT | 1 | 是 |
| `fal-3d` | external_link | unknown | 0 | 是 |
| `fal-generate` | external_link | unknown | 0 | 是 |
| `fal-image-edit` | external_link | unknown | 0 | 是 |
| `fal-realtime` | external_link | unknown | 0 | 是 |
| `fal-train` | external_link | unknown | 0 | 是 |
| `fal-tryon` | external_link | unknown | 0 | 是 |
| `gif-sticker-maker` | stub | MIT | 0 | 是 |
| `imagegen` | external_link | unknown | 0 | 是 |
| `imagen` | external_link | unknown | 0 | 是 |
| `pixelbin-media` | external_link | unknown | 0 | 是 |
| `replicate` | stub | Apache-2.0 | 0 | 是 |
| `venice-image-edit` | stub | MIT | 0 | 是 |
| `venice-image-generate` | stub | MIT | 0 | 是 |
| `fal-restore` | external_link | unknown | 0 | 是 |
| `fal-upscale` | external_link | unknown | 0 | 是 |
| `fal-vision` | external_link | unknown | 0 | 是 |
| `image-enhancer` | external_link | unknown | 0 | 是 |
| `full-page-screenshot` | external_link | unknown | 0 | 是 |
| `screenshot` | stub | Apache-2.0 | 0 | 是 |
| `screenshots-marketing` | external_link | unknown | 0 | 是 |
| `fal-kling-o3` | external_link | unknown | 0 | 是 |
| `fal-lip-sync` | external_link | unknown | 0 | 是 |
| `fal-video-edit` | external_link | unknown | 0 | 是 |
| `sora` | external_link | unknown | 0 | 是 |
| `venice-video` | stub | MIT | 0 | 是 |
| `frame-data-chart-nyt` | bundled_content | Apache-2.0 | 0 | 是 |
| `frame-flowchart-sticky` | bundled_content | Apache-2.0 | 0 | 是 |
| `frame-glitch-title` | bundled_content | Apache-2.0 | 0 | 是 |
| `frame-light-leak-cinema` | bundled_content | Apache-2.0 | 0 | 是 |
| `frame-liquid-bg-hero` | bundled_content | Apache-2.0 | 0 | 是 |
| `frame-logo-outro` | bundled_content | Apache-2.0 | 0 | 是 |
| `frame-macos-notification` | bundled_content | Apache-2.0 | 0 | 是 |
| `remotion` | external_link | Remotion License（自定义，部分公司需付费授权） | 0 | 是 |
| `vfx-text-cursor` | bundled_content | Apache-2.0 | 0 | 是 |
| `video-hyperframes` | bundled_content | Apache-2.0 | 0 | 是 |
| `video-downloader` | external_link | unknown | 0 | 是 |
| `youtube-clipper` | stub | MIT | 0 | 是 |
| `deck-guizang-editorial` | bundled_content | Apache-2.0 | 0 | 是 |
| `deck-open-slide-canvas` | bundled_content | Apache-2.0 | 0 | 是 |
| `deck-swiss-international` | bundled_content | Apache-2.0 | 0 | 是 |
| `frontend-slides` | stub | MIT | 0 | 是 |
| `ppt-keynote` | bundled_content | Apache-2.0 | 0 | 是 |
| `nanobanana-ppt` | external_link | unknown | 0 | 是 |
| `pptx` | external_link | Proprietary (© Anthropic, all rights reserved) | 0 | 是 |
| `pptx-generator` | stub | MIT | 0 | 是 |
| `slides` | external_link | unknown | 0 | 是 |
| `8-bit-orbit-video-template` | bundled_content | Apache-2.0 | 0 | 是 |
| `after-hours-editorial-template` | bundled_content | Apache-2.0 | 0 | 是 |
| `swiss-user-research-video-template` | bundled_content | Apache-2.0 | 0 | 是 |
| `weread-year-in-review-video-template` | bundled_content | Apache-2.0 | 0 | 是 |
| `digits-fintech-swiss-template` | bundled_content | Apache-2.0 | 0 | 是 |
| `editorial-burgundy-principles-template` | bundled_content | Apache-2.0 | 0 | 是 |
| `html-ppt-retro-quarterly-review` | bundled_content | Apache-2.0 | 0 | 是 |
| `swiss-creative-mode-template` | bundled_content | Apache-2.0 | 0 | 是 |
| `field-notes-editorial-template` | bundled_content | Apache-2.0 | 0 | 是 |
| `chat-motion-overlay` | bundled_content | Apache-2.0 | 0 | 是 |
| `export-download-debugging` | bundled_content | Apache-2.0 | 0 | 是 |
| `pptx-html-fidelity-audit` | bundled_content | Apache-2.0 | 0 | 是 |
| `pr-feedback-quality-gate` | bundled_content | Apache-2.0 | 0 | 是 |
| `library-curator` | bundled_content | Apache-2.0 | 0 | 是 |
| `od-next-media-inputs` | bundled_content | Apache-2.0 | 0 | 是 |
| `ai-music-album` | stub | CC0-1.0 | 0 | 是 |
| `venice-audio-music` | stub | MIT | 0 | 是 |
| `speech` | stub | Apache-2.0 | 0 | 是 |
| `venice-audio-speech` | stub | MIT | 0 | 是 |
| `brand-extract` | bundled_content | Apache-2.0 | 0 | 是 |

## 精选 ZIP 核对结果

`v0.1.0-preview.2` 内含 LICENSE、NOTICE；三项技能的全部 8 个源文件均与 release.json 的哈希一致，三项名称均见于包内 NOTICE。已保存的上游源文件比对见 [selected-source-check.json](upstream/selected-source-check.json)。

本轮没有以“有 NOTICE”推导其余 160 项均已许可合规，也没有更改原作者或伪造 Git 提交贡献。
