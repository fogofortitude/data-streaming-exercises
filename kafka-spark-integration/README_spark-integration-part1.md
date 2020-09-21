<h1 id="user-content-scenario-1">Scenario 1</h1>
<p>Given problem: We're given a hypothetical Spark streaming application. This application receives data from Kafka. Every 2 minutes, you can see that Kafka is producing 60000 records. But at its maximum load, the application takes between 2 minutes for each micro-batch of 500 records. How do we improve the speed of this application?</p>
<ol>
<li>
<p><strong>We can tweak the application's algorithm to speed up the application.</strong></p>
<ul>
<li><strong>Let's say the application's algorithm is tweaked - how can you check if most or all of the CPU cores are working?</strong></li>
<li><strong><span style="color: #666699;">Answer:&nbsp;&nbsp;</span></strong>
<ul>
<li><span style="color: #666699;">In a Spark Streaming job, Kafka partitions map 1:1 with Spark partitions. </span></li>
<li><span style="color: #666699;">So we can <span style="text-decoration: underline;">increase Parallelism by increasing the number of partition</span>s in Kafka, <span style="text-decoration: underline;">which then will increase Spark partitions</span>.</span></li>
</ul>
</li>
</ul>
</li>
<li>
<p>We can <strong>check if the input data was balanced/unbalanced</strong>, skewed or not.</p>
</li>
<li>
<p>We can <strong>check the throughput of each partition using Spark UI, and how many cores are consistently working. </strong></p>
<ul>
<li>
<p><span style="color: #666699;">You can also use the&nbsp;<code>htop</code>&nbsp;command to see if your cores are all working (if you have a small cluster).</span></p>
</li>
</ul>
</li>
<li>
<p><strong>We can Increase driver and executor memory:</strong></p>
<ul>
<li>Out-of-memory issues can be frequently solved by increasing the memory of executor and driver.</li>
<li>Always try to give some overhead (usually 10%) to fit your excessive applications.</li>
<li>Application properties you can use for memory management include:
<ul>
<li>spark.executor.memory</li>
<li>spark.driver.memory</li>
</ul>
</li>
</ul>
</li>
<li>
<p>You could also <strong>set&nbsp;<code>spark.streaming.kafka.maxRatePerPartition</code>&nbsp;to a higher number</strong> and see if there is any increase in data ingestion.</p>
</li>
</ol>
<p>&nbsp;</p>
<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="ltr">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<h1 id="scenario-2">Scenario 2</h1>
<p>Other methods of improving your Spark application are by improving system stability and studying your data.</p>
<p>When the heap gets very big (&gt; 32GB), the cost of GC (garbage collection) gets large as well. We might see this when the join application runs with large shuffles (&gt; 20GB), and the GC time will spike.</p>
<p>Can you use a sample of your data? How about using&nbsp;<strong>salting</strong>&nbsp;or&nbsp;<strong>broadcasting</strong>? Let&rsquo;s discuss these below.</p>
<p>In the ideal world, when you operate a join on your dataset, join keys will be evenly distributed and each partition will be nicely organized. In the real world, uneven partitioning is unavoidable due to the nature of your dataset.</p>
<p>Using the Spark UI (or even just your logs), you'll commonly see the errors below:</p>
<ul>
<li>Frozen stages</li>
<li>Low utilization of CPU (workers not working)</li>
<li>Out of memory errors</li>
</ul>
<p>Carefully studying your data, to minimize the skewed data problem, we can try the following:</p>
<ul>
<li>
<p><span style="color: #333399;"><strong>Broadcasting</strong>: You can increase the autoBroadcastJoinThreshold value in spark.sql property so that the smaller tables get &ldquo;broadcasted.&rdquo; This is helpful when you have a large dataset that will not fit into your memory.</span></p>
</li>
<li>
<p><span style="color: #333399;"><strong>Salting</strong>: If you have a key with high cardinality, your dataset will be skewed. Now you introduce a &ldquo;salt,&rdquo; modifying original keys in a certain way and using hash partitioning for proper redistribution of records.</span></p>
</li>
</ul>
<p>Now that we have cleaned up our data and the skew problem as much as we could, and also assuming that our code is optimized, let&rsquo;s talk about how we can stabilize the system through a couple of different methods:</p>
<ul>
<li>Auto scaling</li>
<li>Speculative execution</li>
</ul>
<p><span style="color: #333399;"><strong>Auto scaling</strong> </span></p>
<ul>
<li><span style="color: #333399;">is only doable with cloud clusters as you can always add more nodes freely.</span></li>
<li><span style="color: #333399;">Two popular tech stacks that are used are AWS Auto Scaling (if AWS EMR clusters are used) or auto scaling with Kubernetes (a container-orchestration system).</span></li>
</ul>
<p><span style="color: #333399;"><strong>Speculative execution&nbsp;</strong></span></p>
<ul>
<li><span style="color: #333399;">is another popular addition to stabilize and reduce bottleneck-like threshold. </span></li>
<li><span style="color: #333399;">Speculative execution in Spark detects the &ldquo;speculated task&rdquo; (which means this task is running slower than the median speed of the other tasks), and then submits the &ldquo;speculated task&rdquo; to another worker. </span></li>
<li><span style="color: #333399;">This enables continuous parallel execution rather than shutting off the slow task.</span></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="ltr">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<h2 id="notes-on-scenario-2-diagram-below">Notes on Scenario 2 diagram below</h2>
<p>In this sample image below, let&rsquo;s say task 1 and 2 are identical to each other.</p>
<ul>
<li>In fact, task 2 is a duplicate of task 1.</li>
<li>In the node that contains task 1, if the task is seen to be slower than the median speed, then the job scheduler launches the task 2 (duplicate of task 1) in another node.</li>
<li>If the duplicate task is faster, the result of task 2 will be submitted to the job scheduler. If the original task is faster, then the result of task 1 will be used.</li>
<li>In Spark UI, whichever node that was killed due to late execution will be noted as&nbsp;<code>killed intentionally</code>.</li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="image-atom--image-atom--1XDdu" tabindex="0" role="button" aria-label="Show Image Fullscreen">
<div class="image-atom-content--CDPca">
<div class="image-and-annotations-container--1U01s">&nbsp;</div>
<div class="image-and-annotations-container--1U01s">&nbsp;</div>
</div>
</div>
</div>
</div>
</div>
