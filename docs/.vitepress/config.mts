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
      { text: 'Java8', link: '/java8/index', activeMatch: '/java8/' },
      { text: 'Java21', link: '/java21/index', activeMatch: '/java21/' },
      { text: 'Java 混合编程', link: '/javaMix/README', activeMatch: '/javaMix/' },
    ],

    sidebar: {
      '/java8/': [
        {
          text: 'Java 8',
          items: [
            { text: 'README', link: '/java8/index' },
            { text: 'Date', link: '/java8/Date' },
            { text: 'lambda', link: '/java8/lambda' },
            { text: 'Stream', link: '/java8/Stream' },
          ]
        },
      ],
      '/java21/': [
        {
          text: 'Java 21',
          items: [
            { text: 'README', link: '/java21/index' },
            { text: 'Virtual Threads', link: '/java21/Virtual Threads' }
          ]
        },
      ],
      '/javaMix/': [
        {
          text: 'Java 混合编程',
          items: [
            { text: 'README', link: '/javaMix/README' },
            { text: 'Groovy', link: '/javaMix/Groovy' },
            { text: 'Kotlin', link: '/javaMix/Kotlin' },
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
