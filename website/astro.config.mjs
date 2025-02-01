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
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'Overview', slug: 'getting-started/overview' },
						{ label: 'FAQ', slug: 'getting-started/faq' },
					],
				},
				{
					label: 'Printers',
					autogenerate: { directory: 'printers' },
				},
			],
		}),
	],
});
