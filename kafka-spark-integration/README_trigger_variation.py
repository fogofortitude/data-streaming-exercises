<h2 id="exercise-exploring-triggers">Exercise: Exploring Triggers</h2>
<p>Using the Kafka Server and Structured Streaming application, we will now play with the triggers.</p>
<p>Again, you can use any Kafka library (pykafka, kafka, kafka-confluent, etc). But if you wish to use a library other than kafka-confluent or kafka-python, you will have to reinstall the library each time you wake up workspace (or anytime after you've refreshed, or woken up, or reset data, or used the "Get New Content" button). The idea here is for you to generate a Python file that has a Kafka producer, and this file should act as your bootstrap server.</p>
<p>Please note: If you encounter this error</p>
<pre><code>ImportError: cannot <span class="hljs-keyword">import</span> name <span class="hljs-string">'SourceDistribution'</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'pip._internal.distributions.source'</span> (<span class="hljs-regexp">/opt/</span>conda<span class="hljs-regexp">/lib/</span>python3.<span class="hljs-number">7</span><span class="hljs-regexp">/site-packages/</span>pip<span class="hljs-regexp">/_internal/</span>distributions<span class="hljs-regexp">/source/</span>__init__.py)
</code></pre>
<p>while installing any packages, please run this command:</p>
<pre><code>conda install <span class="hljs-tag">&lt;<span class="hljs-title">package_name</span>&gt;</span></code></pre>

<p>&nbsp;</p>
