什么情况下会发生栈内存溢出。什么时候发生堆溢出？你是怎么排错的？
JVM怎么判断对象是可回收对象？有哪些方法。
JVM的内存结构，新生代与老年代的比例，Eden和Survivor比例。
你知道哪几种垃圾收集器，各自的优缺点，重点讲下cms和G1，包括原理，流程，优缺点。
简单说说你了解的类加载器，可以打破双亲委派么，怎么打破。
JVM内存为什么要分成新生代，老年代，持久代。新生代中为什么要分为Eden和Survivor。
JVM 出现 fullGC 很频繁，怎么去线上排查问题？
JVM中一次完整的GC流程是怎样的，对象如何晋升到老年代，说说你知道的几种主要的JVM参数。
垃圾回收算法的实现原理。
JVM内存模型的相关知识了解多少，比如重排序，内存屏障，happen-before，主内存，工作内存等。
说一下Java对象的创建过程
你们线上应用的JVM参数配置了哪些。
G1和cms区别。
怎么打出线程栈信息。
说一下类加载的执行过程
JVM垃圾回收机制，何时触发MinorGC等操作呢？
ZGC 垃圾收集器，了解过吗
对象的访问定位有哪两种方式?
说一下 jvm 调优的工具？
对象什么时候会进入老年代？
内存泄漏和内存溢出区别？
什么是tomcat类加载机制？
了解逃逸分析技术吗
调用System.gc()会发生什么?
谈谈Minor GC条件，full GC条件
Stop The World 了解过吗？
谈谈你认识多少种OOM？如何避免OOM?
了解过JVM调优没，基本思路是什么?如何确定它们的大小呢？
淘宝热门商品信息在JVM哪个内存区域
字节码的编译过程
Java需要开发人员回收内存垃圾吗？
Java中垃圾回收有什么目的？什么时候进行垃圾回收？
System.gc()和Runtime.gc()会做什么事情？
主内存与工作内存
内存间交互操作
volatile 禁止内存重排序
内存模型三大特性
谈谈先行发生原则
JVM 堆内存溢出后，其他线程是否可继续工作？
说一下JVM 常用参数有哪些？
VM 为什么使用元空间替换了永久代？
Java堆的结构是什么样子的？什么是堆中的永久代(Perm Gen space)?
JVM的永久代中会发生垃圾回收么？
什么是字节码？采用字节码的最大好处是什么？什么Java是虚拟机？
MinorGC 的过程
CPU 占用过高如何分析
Serial与Parallel GC之间的不同之处？
WeakHashMap 是怎么工作的？
解释 Java 堆空间及 GC？
你能保证 GC 执行吗？
JVM中哪个参数是用来控制线程的栈堆栈小的?