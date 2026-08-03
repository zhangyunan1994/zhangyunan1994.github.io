import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "张瑀楠",
  description: "骑摩托不会堵车 - 个人技术文档与随笔",
  lastUpdated: true,
  themeConfig: {
    search: {
      provider: 'local'
    },

    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: '一千零一夜', link: '/jottings/README', activeMatch: '/jottings/' },
      { text: 'Go', link: '/go/Gin 解决跨域问题跨域配置', activeMatch: '/go/' },
      { text: 'Java8', link: '/java8/index', activeMatch: '/java8/' },
      { text: 'Java21', link: '/java21/index', activeMatch: '/java21/' },
      { text: 'Java 混合编程', link: '/javaMix/README', activeMatch: '/javaMix/' },
    ],

    sidebar: {
      '/jottings/': [
        {
          text: '一千零一夜',
          items: [
            { text: 'README', link: '/jottings/README' },
            { text: '第一夜 总纲', link: '/jottings/01 第一夜 总纲' },
            { text: '第二夜 编程伊始', link: '/jottings/02 第二夜 编程伊始' },
            { text: '第三夜 十三信徒', link: '/jottings/03 第三夜 十三信徒' },
            { text: '第四夜 初入峰鸟', link: '/jottings/04 第四夜 初入峰鸟' },
            { text: '第五夜 宿舍趣事', link: '/jottings/05 第五夜 宿舍趣事' },
            { text: '第六夜 大学前夕', link: '/jottings/06 第六夜 大学前夕' },
            { text: '第七夜 连标题都是谎言', link: '/jottings/07 第七夜 连标题都是谎言' },
            { text: '第八夜 第一桶金', link: '/jottings/08 第八夜 第一桶金' },
            { text: '第九夜 我的信条', link: '/jottings/09 第九夜 我的信条' },
            { text: '第十夜 自律下的自由 辞别 2020 计划 2021', link: '/jottings/10 第十夜 自律下的自由 辞别 2020 计划 2021' },
            { text: '第十一夜 我梦见你离开', link: '/jottings/11 第十一夜 我梦见你离开' },
            { text: '第十二夜 我的故事一直有你们', link: '/jottings/12 第十二夜 我的故事一直有你们' },
          ]
        },
      ],
      '/go/': [
        {
          text: 'Go',
          items: [
            { text: 'Gin 解决跨域问题跨域配置', link: '/go/Gin 解决跨域问题跨域配置' },
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
    ],

    footer: {
      message: 'Released under the CC License.',
      copyright: 'Copyright © 2023-present zhangyunan'
    }
  }
})
