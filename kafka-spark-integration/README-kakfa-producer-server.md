<h3><strong>Exercise - Create a Kafka Producer Server</strong></h3>
<p><br />In this workspace, you&rsquo;re going to create a Kafka Producer Server. You&rsquo;ll be using this code for the next few workspace exercises. You have already learned how to create a Kafka Producer Server in the previous Kafka course, so refer back to those lessons if you need to! We&rsquo;re just starting you with an empty Python file for this exercise, but you can refer to the solution code if you really need to. (Try not to!)</p>
<h4>Requirements:</h4>
<ul style="list-style-type: circle;">
<li>Your Kafka Server should ingest the <span style="color: #808080;"><em>uber.json</em></span> data file in the workspace correctly. If unsure of the correct path of the file, type <em><span style="color: #808080;">pwd</span></em> in the console to get the absolute path of the file.</li>
<li>You can name your own topic and feel free to use any free port number for this server.</li>
<li>This will be your bootstrap server for your streaming application.<br />You should be able to check if your server ingests data correctly by using Kafka Consumer Console.</li>
<li>You can use any Kafka library (pykafka, kafka, kafka-confluent, etc). But if you wish to use a library other than kafka-confluent or kafka-python, you will have to reinstall the library each time you wake up workspace (or anytime after you've refreshed, or woken up, or reset data, or used the "Get New Content" button). The idea here is for you to generate a Python file that has a Kafka producer, and this file should act as your bootstrap server.</li>
</ul>
<p>&nbsp;</p>
<p><strong>Please note:</strong> If you encounter this error</p>
<blockquote>
<p style="padding-left: 30px;"><span style="color: #808080;">ImportError: cannot import name 'SourceDistribution' from 'pip._internal.distributions.source' (/opt/conda/lib/python3.7/site-packages/pip/_internal/distributions/source/__init__.py)</span></p>
</blockquote>
<p><br /><strong>while installing any packages, please run this command:</strong></p>
<blockquote>
<p><span style="color: #808080;">conda install &lt;package_name&gt;</span></p>
</blockquote>

<p>&nbsp;</p>
<h4 class="anchor-heading"><a href="https://kafka.apache.org/quickstart#quickstart_startserver">How to Start a KAFKA Environment</a></h4>
<p class="note"><strong>NOTE:</strong> Your local environment must have Java 8+ installed.</p>
<p>Run the following commands in order to start all services in the correct order:</p>
<pre class="line-numbers  language-bash"><span style="color: #999999;"><code class="  language-bash"><span class="token comment"># Start the ZooKeeper service</span>
<span class="token comment"># Note: Soon, ZooKeeper will no longer be required by Apache Kafka.</span>
$ bin/zookeeper-server-start.sh config/zookeeper.properties</code></span></pre>
<p>Open another terminal session and run:</p>
<pre class="line-numbers  language-bash"><span style="color: #999999;"><code class="  language-bash"><span class="token comment"># Start the Kafka broker service</span>
$ bin/kafka-server-start.sh config/server.properties</code></span></pre>
<p>Once all services have successfully launched, you will have a basic Kafka environment running and ready to use.</p>
