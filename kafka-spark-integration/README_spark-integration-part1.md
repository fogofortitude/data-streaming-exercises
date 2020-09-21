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
</ul>
</li>
<li>
<p>You could also <strong>set&nbsp;<code>spark.streaming.kafka.maxRatePerPartition</code>&nbsp;to a higher number</strong> and see if there is any increase in data ingestion.</p>
</li>
</ol>
