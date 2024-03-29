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
      { text: '个人记录', link: '/jottings/README', activeMatch: '/jottings/' },
      { text: 'Go', link: '/go/README', activeMatch: '/go/' },
      { text: 'Netty', link: '/netty/README', activeMatch: '/netty/' },
      { text: 'Java8', link: '/java8/index', activeMatch: '/java8/' },
      { text: 'Java21', link: '/java21/index', activeMatch: '/java21/' },
      { text: 'Java 混合编程', link: '/javaMix/README', activeMatch: '/javaMix/' },
    ],

    sidebar: {
      '/jottings/': [
        {
          text: '一千零一夜',
          items: [
            { text: '第一夜 总纲', link: '/jottings/01 第一夜 总纲' },
            { text: 'lambda', link: '/java8/lambda' },
            { text: 'Stream', link: '/java8/Stream' },
          ]
        },
      ],
      '/go/': [
        {
          text: 'Go',
          items: [
            { text: '第一夜 总纲', link: '/go/' },
            { text: 'Gin 解决跨域问题跨域配置', link: '/java8/Gin 解决跨域问题跨域配置' },
          ]
        },
      ],
      '/java8/': [
        {
          text: 'Java 8',
          items: [
            { text: 'README', link: '/java8/index' },
            { text: '时间相关', link: '/java8/Date' },
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
            { text: '虚拟线程 Virtual Threads', link: '/java21/Virtual Threads' },
            { text: '结构化并发（预览）', link: '/java21/Virtual Threads' },
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
