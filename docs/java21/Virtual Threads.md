# Virtual Threads

```java:line-numbers {5,6}

// 线程池
ExecutorService es = Executors.newFixedThreadPool(10);

// 虚拟线程
ExecutorService ves = Executors.newVirtualThreadPerTaskExecutor();

```


```java:line-numbers {3-5}
PrivilegedAction<ForkJoinPool> pa = () -> {
    int parallelism, maxPoolSize, minRunnable;
    String parallelismValue = System.getProperty("jdk.virtualThreadScheduler.parallelism");
    String maxPoolSizeValue = System.getProperty("jdk.virtualThreadScheduler.maxPoolSize");
    String minRunnableValue = System.getProperty("jdk.virtualThreadScheduler.minRunnable");
    if (parallelismValue != null) {
        parallelism = Integer.parseInt(parallelismValue);
    } else {
        parallelism = Runtime.getRuntime().availableProcessors();
    }
    if (maxPoolSizeValue != null) {
        maxPoolSize = Integer.parseInt(maxPoolSizeValue);
        parallelism = Integer.min(parallelism, maxPoolSize);
    } else {
        maxPoolSize = Integer.max(parallelism, 256);
    }
    if (minRunnableValue != null) {
        minRunnable = Integer.parseInt(minRunnableValue);
    } else {
        minRunnable = Integer.max(parallelism / 2, 1);
    }
    Thread.UncaughtExceptionHandler handler = (t, e) -> { };
    boolean asyncMode = true; // FIFO
    return new ForkJoinPool(parallelism, factory, handler, asyncMode,
                    0, maxPoolSize, minRunnable, pool -> true, 30, SECONDS);
};
```

## ForkJoinPool 配置说明

```java
ForkJoinPool(int parallelism,
    ForkJoinWorkerThreadFactory factory,
    UncaughtExceptionHandler handler,
    boolean asyncMode,
    int corePoolSize,
    int maximumPoolSize,
    int minimumRunnable,
    Predicate<? super ForkJoinPool> saturate,
    long keepAliveTime,
    TimeUnit unit)
```





1. parallelism 并行级别。 对于默认值，Runtime#availableProcessors
2. factory 用于创建新线程的工厂。 为了
      * 默认值，使用{@link #defaultForkJoinWorkerThreadFactory}。
      *
3. handler 内部工作线程的处理程序
      * 由于遇到不可恢复的错误而终止
      * 执行任务。 对于默认值，请使用 {@code null}。
      *
4. asyncMode 如果为 true，则建立本地先进先出
      * 从未加入的分叉任务的调度模式。 这
      * 模式可能比默认的基于本地堆栈的模式更合适
      *工作线程仅处理的应用程序中的模式
      * 事件式异步任务。 对于默认值，请使用 {@code
      * 错误的}。
      *
5. corePoolSize 池中保留的线程数
      *（除非在保持活动状态后超时）。 通常（并且
      * 默认情况下）这与并行级别的值相同，
      * 但可以设置为更大的值以减少动态开销，如果
      * 任务经常阻塞。 使用较小的值（例如
      * {@code 0}) 与默认效果相同。
      *
6. maxPoolSize 允许的最大线程数。
      * 当达到最大值时，尝试替换阻塞的
      * 线程失败。 （但是，因为创建和终止
      * 不同的线程可能重叠，并且可能由给定的管理
      * 线程工厂，这个值可能会暂时超过。）
      * 安排与公共默认使用的值相同的值
      * 池，使用 {@code 256} 加上 {@code 并行度} 级别。 （经过
      * 默认情况下，公共池最多允许256个备用
      * 线程。）使用一个值（例如 {@code
      * Integer.MAX_VALUE}) 大于实现的总数
      * 线程限制与使用此限制具有相同的效果（即
      * 默认）。
      *
7. minimumRunnable 允许的最小核心数
      * 线程未被连接或{@link ManagedBlocker}阻止。 到
      * 当未阻塞的线程太少时确保进度，并且
      * 可能存在未执行的任务，构造新线程，最多
      * 给定的最大池大小。 对于默认值，请使用 {@code
      * 1}，确保活性。 更大的值可能会改善
      * 存在阻塞活动时的吞吐量，但可能
      * 不是，因为开销增加。 零值可能是
      * 当提交的任务不能有依赖关系时可以接受
      * 需要额外的线程。
      *
8. saturate if non-null, 尝试调用的谓词
      * 创建超过允许的最大线程总数。 经过
      * 默认情况下，当线程即将在连接或{@link
      * ManagedBlocker}，但无法替换，因为
      * 将超出最大池大小，{@link
      * 抛出RejectedExecutionException}。 但如果这个谓词
      * 返回{@code true}，则不会抛出异常，因此池
      * 继续运营，但数量少于目标数量
      * 可运行的线程，这可能无法确保进度。
      *
9. keepAliveTime 自上次使用以来经过的时间
      * 线程被终止（然后根据需要替换）。
      * 对于默认值，请使用 {@code 60, TimeUnit.SECONDS}。
      *
10. unit {@code keepAliveTime} 参数的时间单位
      *
      * 如果并行度小于或则抛出IllegalArgumentException
      * 等于零，或大于实施限制，
      * 或者如果 MaximumPoolSize 小于并行度，
      * 如果 keepAliveTime 小于或等于 0。
      * 如果工厂为 null，则抛出 NullPointerException
      * 如果安全管理器存在并且@抛出SecurityException
      * 调用者不允许修改线程
      *因为它不包含{@link
      * java.lang.RuntimePermission}{@code("modifyThread")}

11. jdk.virtualThreadScheduler.parallelism: 线程数量，默认为当前系统的 CPU 数量。
12. jdk.virtualThreadScheduler.maxPoolSize: 最大线程数量，默认为 Integer.MAX_VALUE
13. jdk.virtualThreadScheduler.minRunnable:

