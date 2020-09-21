<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="ltr">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<h1 id="scenario-1">Scenario 1</h1>
<p>Given problem: We're given a hypothetical Spark streaming application. This application receives data from Kafka. Every 2 minutes, you can see that Kafka is producing 60000 records. But at its maximum load, the application takes between 2 minutes for each micro-batch of 500 records. How do we improve the speed of this application?</p>
<ol>
<li>
<p>We can tweak the application's algorithm to speed up the application.</p>
<ul>
<li>Let's say the application's algorithm is tweaked - how can you check if most or all of the CPU cores are working?
<ul>
<li>In a Spark Streaming job, Kafka partitions map 1:1 with Spark partitions. So we can increase Parallelism by increasing the number of partitions in Kafka, which then will increase Spark partitions.</li>
</ul>
</li>
</ul>
</li>
<li>
<p>We can check if the input data was balanced/unbalanced, skewed or not. We can check the throughput of each partition using Spark UI, and how many cores are consistently working. You can also use the&nbsp;<code>htop</code>&nbsp;command to see if your cores are all working (if you have a small cluster).</p>
<ul>
<li>Increase driver and executor memory: Out-of-memory issues can be frequently solved by increasing the memory of executor and driver. Always try to give some overhead (usually 10%) to fit your excessive applications.</li>
</ul>
</li>
<li>
<p>You could also set&nbsp;<code>spark.streaming.kafka.maxRatePerPartition</code>&nbsp;to a higher number and see if there is any increase in data ingestion.</p>
</li>
</ol>
</div>
</div>
</div>
</div>
</div>
<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="container--3sWx1">
<div class="prompt--1YMnx">
<h3 class="question-number--3IlDk">&nbsp;</h3>
</div>
</div>
</div>
</div>
</div>
