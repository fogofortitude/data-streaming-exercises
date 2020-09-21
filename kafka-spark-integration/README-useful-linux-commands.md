<h2 id="SparkUsefulLinuxTerminalCommands-HowtostartupaZookeeperServer"><strong>How to startup a Zookeeper Server</strong></h2>
<div class="code panel pdl conf-macro output-block" data-hasbody="true" data-macro-name="code">
<div class="codeContent panelContent pdl">
<div>
<div id="highlighter_807956" class="syntaxhighlighter sh-rdark nogutter  text">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="code">
<div class="container" title="Hint: double-click to select code">
<div class="line number1 index0 alt2"><code class="text plain">/usr/bin/zookeeper-server-start /etc/kafka/zookeeper.properties</code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
<p>log.dirs=/var/lib/kafka/data</p>
<p>cd /var/log/&nbsp;</p>
<h2 id="SparkUsefulLinuxTerminalCommands-HowtostartupaKakfaServer"><strong>How to startup a Kakfa Server</strong></h2>
<div class="code panel pdl conf-macro output-block" data-hasbody="true" data-macro-name="code">
<div class="codeContent panelContent pdl">
<div>
<div id="highlighter_718410" class="syntaxhighlighter sh-rdark nogutter  text">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="code">
<div class="container" title="Hint: double-click to select code">
<div class="line number1 index0 alt2"><code class="text plain">/usr/bin/kafka-server-start /etc/kafka/server.properties</code></div>
</div>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h2 id="SparkUsefulLinuxTerminalCommands-Howtoidentifyifaprocessislisteningtoaport"><strong>How to identify if a process is listening to a port</strong></h2>
<h2 id="SparkUsefulLinuxTerminalCommands-lsofcommand"><strong>lsof command</strong></h2>
<div class="confluence-information-macro confluence-information-macro-tip conf-macro output-block" data-hasbody="true" data-macro-name="tip">
<div class="confluence-information-macro-body">
<p>To identify&nbsp;whether or not any process is listening to a particular port; you can run lsof commands.&nbsp;</p>
<p>For example</p>
<p><strong>For Zookeeper Server</strong></p>
<div class="code panel pdl conf-macro output-block" data-hasbody="true" data-macro-name="code">
<div class="codeContent panelContent pdl">
<div>
<div id="highlighter_7021" class="syntaxhighlighter sh-rdark nogutter  powershell">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="code">
<div class="container" title="Hint: double-click to select code">
<div class="line number1 index0 alt2"><code class="powershell plain">lsof&nbsp;</code><code class="powershell keyword">-i</code>&nbsp;<code class="powershell plain">tcp:2181</code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
<p><strong>For Kafka Server</strong></p>
<div class="code panel pdl conf-macro output-block" data-hasbody="true" data-macro-name="code">
<div class="codeContent panelContent pdl">
<div>
<div id="highlighter_193468" class="syntaxhighlighter sh-rdark nogutter  powershell">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="code">
<div class="container" title="Hint: double-click to select code">
<div class="line number1 index0 alt2"><code class="powershell plain">lsof&nbsp;</code><code class="powershell keyword">-i</code>&nbsp;<code class="powershell plain">tcp:9092</code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
<p>If you find that the command is not recognised you will need to install it:&nbsp;</p>
<div class="code panel pdl conf-macro output-block" data-hasbody="true" data-macro-name="code">
<div class="codeContent panelContent pdl">
<div>
<div id="highlighter_635115" class="syntaxhighlighter sh-rdark nogutter  powershell">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="code">
<div class="container" title="Hint: double-click to select code">
<div class="line number1 index0 alt2"><code class="powershell plain">sudo apt</code><code class="powershell keyword">-get</code>&nbsp;<code class="powershell plain">install lsof</code></div>
</div>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h2 id="SparkUsefulLinuxTerminalCommands-netsatcommand"><strong>netsat command</strong></h2>
<p>netsat is a tool to provide information on network connections including IP, port and servers communicating on these ports</p>
<p><strong>To install it:&nbsp;</strong></p>
<div class="code panel pdl conf-macro output-block" data-hasbody="true" data-macro-name="code">
<div class="codeContent panelContent pdl">
<div>
<div id="highlighter_816235" class="syntaxhighlighter sh-rdark nogutter  powershell">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="code">
<div class="container" title="Hint: double-click to select code">
<div class="line number1 index0 alt2"><code class="powershell plain">sudo apt install net</code><code class="powershell keyword">-tools</code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
<p>&nbsp;</p>
<p><strong>To run it</strong></p>
<div class="code panel pdl conf-macro output-block" data-hasbody="true" data-macro-name="code">
<div class="codeContent panelContent pdl">
<div>
<div id="highlighter_608934" class="syntaxhighlighter sh-rdark nogutter  powershell">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="code">
<div class="container" title="Hint: double-click to select code">
<div class="line number1 index0 alt2"><code class="powershell plain">sudo netsat&nbsp;</code><code class="powershell keyword">-tunlp</code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
<p><strong>Instructions explained</strong></p>
<ul>
<li>-t = show all TCP ports</li>
<li>-u = show all UDP ports</li>
<li>-n =&nbsp;show all numerical / IP ports</li>
<li>-l = show all listening ports</li>
<li>-p = show PID and name of listening ports</li>
</ul>
<p>&nbsp;</p>
<h2 id="SparkUsefulLinuxTerminalCommands-HowtoidentifySparkandScalaversion"><strong>How to identify Spark and Scala version</strong></h2>
<div class="code panel pdl conf-macro output-block" data-hasbody="true" data-macro-name="code">
<div class="codeContent panelContent pdl">
<div>
<div id="highlighter_309427" class="syntaxhighlighter sh-rdark nogutter  powershell">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="code">
<div class="container" title="Hint: double-click to select code">
<div class="line number1 index0 alt2"><code class="powershell plain">spark</code><code class="powershell keyword">-submit</code>&nbsp;<code class="powershell plain">-</code><code class="powershell keyword">-version</code></div>
</div>
</td>
</tr>
</tbody>
</table>
<p>&nbsp;</p>
<h2 id="SparkUsefulLinuxTerminalCommands-HowtosubmitapysparkpackageforKafkaIngestion">How to submit a pyspark package for Kafka Ingestion</h2>
<div class="code panel pdl conf-macro output-block" data-hasbody="true" data-macro-name="code">
<div class="codeContent panelContent pdl">
<div>
<div id="highlighter_158650" class="syntaxhighlighter sh-rdark nogutter  powershell">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="code">
<div class="container" title="Hint: double-click to select code">
<div class="line number1 index0 alt2"><code class="powershell plain">spark</code><code class="powershell keyword">-submit</code>&nbsp;<code class="powershell plain">-</code><code class="powershell keyword">-packages</code>&nbsp;<code class="powershell plain">org.apache.spark:spark</code><code class="powershell keyword">-sql</code><code class="powershell keyword">-kafka</code><code class="powershell plain">-0-10_2.11:2.3.4 ingest_kafka_data.py</code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="code">
<div class="container" title="Hint: double-click to select code">
<div class="line number1 index0 alt2"><code class="powershell plain"></code></div>
<div class="line number1 index0 alt2"><code class="powershell plain">spark</code><code class="powershell keyword">-submit</code>&nbsp;<code class="powershell plain">-</code><code class="powershell keyword">-packages</code>&nbsp;<code class="powershell plain">org.apache.spark:spark</code><code class="powershell keyword">-sql</code><code class="powershell keyword">-kafka</code><code class="powershell plain">-0-10_2.11:2.3.4 trigger_variation.py</code></div>
</div>
</td>
</tr>
</tbody>
</table>
<h2 id="SparkUsefulLinuxTerminalCommands-HowtoconfirmyourKafkaIngestionisworking">How to confirm your Kafka Ingestion is working</h2>
<div class="code panel pdl conf-macro output-block" data-hasbody="true" data-macro-name="code">
<div class="codeContent panelContent pdl">
<div>
<div id="highlighter_353692" class="syntaxhighlighter sh-rdark nogutter  powershell">
<table border="0" cellspacing="0" cellpadding="0">
<tbody>
<tr>
<td class="code">
<div class="container" title="Hint: double-click to select code">
<div class="line number1 index0 alt2"><code class="powershell plain">kafka</code><code class="powershell keyword">-console</code><code class="powershell keyword">-consumer</code>&nbsp;<code class="powershell plain">-</code><code class="powershell keyword">-bootstrap</code><code class="powershell keyword">-server</code>&nbsp;<code class="powershell plain">localhost:9092 -</code><code class="powershell keyword">-topic</code>&nbsp;<code class="powershell plain">&lt;your topic name here&gt;&nbsp; -</code><code class="powershell keyword">-from</code><code class="powershell keyword">-beginning</code></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<p>&nbsp;</p>
<p>&nbsp;</p>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
