	O??e?^?@O??e?^?@!O??e?^?@	???&2?????&2??!???&2??"e
=type.googleapis.com/tensorflow.profiler.PerGenericStepDetails$O??e?^?@?=?U???A?):?K?@Y?$???B@*	    ??@2?
JIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[0]::MapQk?w??@@!ɣsS??V@)8gDi?@@1'sO~??V@:Preprocessing2k
4Iterator::Model::MaxIntraOpParallelism::Map::BatchV2KY?8??A@!h?t?.X@)&䃞ͪ??1?E7??]@:Preprocessing2b
+Iterator::Model::MaxIntraOpParallelism::Map?H?}?B@!c???X@)????H??1Z???S
@:Preprocessing2y
BIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip?:M??@@!?SSi??V@)?H?}??1?H???J??:Preprocessing2?
RIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[1]::TensorSlice????ׁ??!]V?]@[??)????ׁ??1]V?]@[??:Preprocessing2?
WIterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle::Zip[0]::Map::TensorSlice????????!??TK??)????????1??TK??:Preprocessing2t
=Iterator::Model::MaxIntraOpParallelism::Map::BatchV2::Shuffle*:?? A@!?????V@)$????ۗ?1Y#Y?E??:Preprocessing2]
&Iterator::Model::MaxIntraOpParallelism?ܵ?|?B@!??Jv??X@)?????g?1F?C???:Preprocessing2F
Iterator::ModelF???ԀB@!      Y@)??_vOf?1)??Cm?}?:Preprocessing:?
]Enqueuing data: you may want to combine small input data chunks into fewer but larger chunks.
?Data preprocessing: you may increase num_parallel_calls in <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map" target="_blank">Dataset map()</a> or preprocess the data OFFLINE.
?Reading data from files in advance: you may tune parameters in the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch size</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave cycle_length</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer_size</a>)
?Reading data from files on demand: you should read data IN ADVANCE using the following tf.data API (<a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#prefetch" target="_blank">prefetch</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/Dataset#interleave" target="_blank">interleave</a>, <a href="https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset#class_tfrecorddataset" target="_blank">reader buffer</a>)
?Other data reading or processing: you may consider using the <a href="https://www.tensorflow.org/programmers_guide/datasets" target="_blank">tf.data API</a> (if you are not using it now)?
:type.googleapis.com/tensorflow.profiler.BottleneckAnalysis?
device?Your program is NOT input-bound because only 1.6% of the total step time sampled is waiting for input. Therefore, you should focus on reducing other time.no*no9???&2??I??e?7?X@Zno#You may skip the rest of this page.B?
@type.googleapis.com/tensorflow.profiler.GenericStepTimeBreakdown?
	?=?U????=?U???!?=?U???      ??!       "      ??!       *      ??!       2	?):?K?@?):?K?@!?):?K?@:      ??!       B      ??!       J	?$???B@?$???B@!?$???B@R      ??!       Z	?$???B@?$???B@!?$???B@b      ??!       JCPU_ONLYY???&2??b q??e?7?X@