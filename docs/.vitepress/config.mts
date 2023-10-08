import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "My Awesome Project",
  description: "A VitePress Site",
  lastUpdated: true,
  themeConfig: {
    search: {
      provider: 'local'
    },

    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Java8', link: '/java8/index' },
      { text: 'Java21', link: '/java21/index' },
    ],

    sidebar: {
      '/java8/': [
        {
          text: 'Java8',
          items: [
            { text: 'README', link: '/java8/index' },
            { text: 'Date', link: '/java8/Date' }
          ]
        },
      ],
      '/java21/': [
        {
          text: 'Java21',
          items: [
            { text: 'README', link: '/java21/index' },
            { text: 'Virtual Threads', link: '/java21/Virtual Threads' }
          ]
        },
      ]
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/zhangyunan1994' },
      { icon: 'twitter', link: 'https://github.com/zhangyunan1994' }
    ],

    footer: {
      message: 'Released under the CC License.',
      copyright: 'Copyright © 2023-present zhangyunan'
    }
  }
})
