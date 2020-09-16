<div>
<div class="index--container--2OwOl">
<div class="index--atom--lmAIo layout--content--3Smmq">
<div class="ltr">
<div class="index-module--markdown--2MdcR ureact-markdown ">
<h3 id="exercise-kafka-source-provider">Exercise: Kafka Source Provider</h3>
<p>Using the Kafka Producer Server you created in the previous exercise, we can now ingest data from the Kafka Producer Server to a Structured Streaming application. First you&rsquo;ll need to set up the entry point for the stream.</p>
<p>Requirements:</p>
<ul>
<li>Set up the entry point</li>
<li>Use appropriate configurations in the options to ingest the Kafka stream</li>
<li>Do a&nbsp;<code>df.printSchema()</code>&nbsp;to explore the schema of the default Kafka ingestion</li>
<li>You can use any Kafka library (pykafka, kafka, kafka-confluent, etc). But if you wish to use a library other than kafka-confluent or kafka-python, you will have to reinstall the library each time you wake up workspace (or anytime after you've refreshed, or woken up, or reset data, or used the "Get New Content" button). The idea here is for you to generate a Python file that has a Kafka producer, and this file should act as your bootstrap server.</li>
</ul>
<p>Please note: If you encounter this error</p>
<pre><code>ImportError: cannot <span class="hljs-keyword">import</span> name <span class="hljs-string">'SourceDistribution'</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'pip._internal.distributions.source'</span> (<span class="hljs-regexp">/opt/</span>conda<span class="hljs-regexp">/lib/</span>python3.<span class="hljs-number">7</span><span class="hljs-regexp">/site-packages/</span>pip<span class="hljs-regexp">/_internal/</span>distributions<span class="hljs-regexp">/source/</span>__init__.py)
</code></pre>
<p>while installing any packages, please run this command:</p>
<pre><code>conda install <span class="hljs-tag">&lt;<span class="hljs-title">package_name</span>&gt;</span>
</code></pre>
</div>
</div>
</div>
</div>
</div>
<div>&nbsp;</div>
