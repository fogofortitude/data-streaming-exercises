<h4 class="anchor-heading"><a href="https://kafka.apache.org/quickstart#quickstart_startserver">How to Start a KAFKA Environment</a></h4>
<p class="note"><strong>NOTE:</strong> Your local environment must have Java 8+ installed.</p>
<p>Run the following commands in order to start all services in the correct order:</p>
<p class="line-numbers  language-bash"><span style="color: #999999;"><code class="  language-bash"></code></span><span style="color: #999999;"><code class="  language-bash"></code></span><span style="color: #999999;"><code class="  language-bash"><br />/usr/bin/zookeeper-server-start /etc/kafka/zookeeper.properties</code></span></p>
<p>Open another terminal session and run:</p>
<pre class="line-numbers  language-bash"><span style="color: #999999;"><code class="  language-bash"><br />/usr/bin/kafka-server-start /etc/kafka/kafka-tools.properties</code></span></pre>
<p>Once all services have successfully launched, you will have a basic Kafka environment running and ready to use./ect</p>
<p>&nbsp;</p>
<p>Alternatively, use&nbsp;<strong>lsof</strong> to check if any process is listening to a particular port.</p>
<blockquote>
<ul>
<li><span style="color: #808080;">lsof -i tcp:2181 -- For Zookeeper</span></li>
<li><span style="color: #808080;">lsof -i tcp:9092 -- For kafka</span></li>
</ul>
</blockquote>
<div class="codeBlockLayout_code-line__38e2J" data-ref="code-line">
<div class="codeBlockLayout_line-number__1006q">&nbsp;</div>
<div class="codeBlockLayout_line-content__1t2_W"><span style="background-color: #808080;">&nbsp;</span></div>
</div>
<div class="codeBlockLayout_code-line__38e2J" data-ref="code-line">
<div class="codeBlockLayout_line-content__1t2_W">&nbsp;</div>
</div>
