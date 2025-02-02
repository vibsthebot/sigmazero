// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'Launchpad',
			social: {
				github: 'https://github.com/qcoral/sigmazero',
			},
			sidebar: [
				{
					label: 'Getting Started',
					autogenerate: { directory: 'getting-started' },
				},
				{
					label: 'Printers',
					autogenerate: { directory: 'printers' },
				},
			],
		}),
	],
});
