def DFS(path, edges, memo):
	v = path[-1]
	if v in memo:
		return memo[v]
	#print path
	for s in edges:
		if v == s[0]:
			#Check if there's a cycle, if there's a cycle, then unable to finish
			if s[1] in path:
				return False
			if DFS(path + [s[1]], edges, memo) == False:
				return False
	#print path
	memo[v] = True
	return True
def canFinish(numCourses, prerequisites):
	'''
	https://leetcode.com/problems/course-schedule/#/description
	https://leetcode.com/submissions/detail/102878591/
	'''
	#vertices = [n[1] for n in prerequisites]
	edges = [[n[1], n[0]] for n in prerequisites] # reverse the prerequisites. n[1] is the start, n[0] is the end
	memo = { }
	#print "edges:", edges
	#print "vertices:", vertices
	for v in range(numCourses):
		if DFS([v], edges, memo) == False:
			return False
	return True
	
def test_canFinish():
	print canFinish(2, [[0,1],[1,0]])
	print canFinish(8, [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]])
	print canFinish(2, [[785,230],[843,838],[725,91],[236,135],[804,544],[779,204],[599,306],[685,651],[716,562],[419,381],[575,549],[895,348],[872,16],[938,344],[565,340],[794,21],[867,557],[857,486],[256,131],[959,439],[756,728],[873,330],[320,99],[825,657],[620,63],[534,404],[795,385],[171,159],[982,854],[458,203],[243,107],[403,289],[868,400],[313,214],[851,368],[773,767],[276,0],[948,672],[439,100],[437,255],[272,175],[758,158],[495,453],[480,158],[240,61],[970,568],[221,215],[758,22],[310,106],[822,111],[229,163],[386,150],[293,94],[950,25],[959,680],[858,78],[819,512],[672,385],[830,353],[961,919],[757,507],[180,98],[755,237],[382,308],[502,260],[987,407],[834,646],[963,895],[348,320],[973,436],[96,32],[916,857],[373,287],[948,205],[277,84],[467,386],[663,289],[763,152],[788,323],[958,514],[757,675],[980,387],[494,78],[883,245],[974,615],[467,153],[763,40],[732,626],[355,244],[751,586],[839,11],[675,13],[52,19],[853,6],[758,296],[534,339],[898,550],[744,59],[822,166],[338,20],[730,149],[979,725],[539,188],[848,413],[798,115],[399,215],[832,268],[709,319],[894,175],[998,373],[858,480],[263,189],[522,25],[613,377],[736,602],[253,94],[375,128],[374,54],[929,463],[722,265],[435,261],[841,780],[585,324],[46,14],[972,142],[811,715],[514,142],[240,142],[423,412],[856,140],[643,149],[570,399],[491,390],[498,303],[919,514],[616,488],[497,447],[235,179],[362,83],[913,323],[767,502],[470,336],[398,2],[702,16],[420,3],[670,74],[942,107],[579,513],[466,252],[775,608],[321,251],[653,22],[955,743],[923,64],[443,48],[817,152],[288,180],[983,660],[223,85],[816,341],[812,247],[733,264],[610,204],[761,400],[652,592],[840,39],[929,325],[814,203],[477,373],[888,337],[722,92],[980,260],[532,181],[886,639],[784,421],[962,531],[784,57],[423,30],[277,172],[558,349],[781,403],[998,216],[864,741],[941,901],[996,413],[944,400],[994,394],[781,612],[607,206],[453,261],[462,160],[534,406],[637,4],[897,713],[867,244],[463,33],[473,462],[149,35],[78,39],[479,91],[832,280],[923,717],[447,147],[254,141],[332,121],[698,196],[576,233],[914,272],[891,149],[447,140],[719,449],[343,274],[935,268],[495,156],[433,59],[969,526],[752,347],[948,291],[734,357],[795,218],[274,47],[863,32],[427,289],[969,859],[453,46],[428,212],[702,152],[773,435],[539,504],[318,14],[733,141],[307,268],[499,482],[713,189],[706,325],[490,349],[970,120],[892,72],[942,484],[771,718],[784,325],[665,543],[530,474],[827,90],[564,360],[247,172],[610,374],[853,700],[364,233],[893,425],[695,530],[382,42],[779,582],[472,17],[988,543],[498,214],[895,532],[851,165],[960,845],[825,470],[626,373],[891,186],[830,658],[986,925],[541,210],[633,606],[847,634],[538,454],[673,25],[417,140],[774,42],[275,143],[608,495],[736,274],[687,403],[882,434],[729,345],[773,502],[955,184],[932,127],[577,524],[705,289],[918,28],[506,441],[663,352],[566,530],[256,255],[206,64],[511,256],[771,393],[732,279],[489,464],[727,451],[653,505],[921,749],[915,537],[906,90],[931,420],[970,543],[624,537],[354,126],[554,373],[699,476],[901,109],[600,388],[179,81],[829,205],[824,549],[987,861],[578,538],[356,147],[666,287],[932,264],[392,138],[779,98],[715,320],[564,509],[646,293],[294,53],[706,472],[548,512],[905,860],[926,804],[715,323],[788,547],[655,419],[813,451],[528,482],[779,93],[908,193],[463,200],[847,284],[231,128],[620,361],[372,169],[435,257],[394,268],[420,368],[850,130],[631,144],[657,63],[423,222],[580,116],[382,334],[385,242],[265,125],[325,125],[209,71],[519,274],[917,870],[779,742],[751,604],[839,281],[483,287],[256,34],[666,389],[913,135],[513,161],[666,170],[426,425],[804,631],[461,280],[507,156],[758,73],[764,306],[905,499],[234,86],[630,252],[876,124],[318,275],[331,301],[874,190],[969,681],[862,302],[885,794],[616,206],[699,142],[877,538],[802,475],[704,424],[479,300],[916,326],[932,573],[845,230],[224,46],[790,401],[795,700],[639,176],[917,471],[652,217],[944,928],[518,110],[661,103],[874,186],[206,72],[730,404],[969,674],[801,770],[535,1],[390,243],[270,211],[626,545],[875,464],[601,484],[630,505],[195,82],[891,703],[545,411],[603,252],[215,177],[729,440],[951,351],[476,42],[876,261],[812,248],[735,110],[386,102],[534,72],[556,310],[326,282],[608,226],[900,17],[667,555],[794,164],[709,304],[907,297],[421,62],[608,102],[289,58],[383,84],[895,254],[694,156],[968,311],[932,139],[657,67],[936,659],[875,759],[483,233],[490,469],[84,40],[321,225],[843,341],[449,255],[719,325],[854,271],[697,47],[594,320],[734,253],[655,552],[302,154],[704,624],[674,308],[790,609],[883,427],[549,417],[972,196],[933,119],[999,40],[760,745],[543,84],[994,19],[506,343],[440,121],[947,54],[713,289],[642,210],[810,410],[820,808],[964,684],[963,709],[347,292],[973,503],[943,204],[728,577],[851,741],[549,215],[415,40],[957,439],[279,181],[931,883],[840,84],[742,555],[803,196],[884,332],[708,352],[643,192],[976,278],[693,665],[661,462],[792,538],[961,238],[133,107],[561,180],[860,508],[924,616],[870,660],[776,369],[793,307],[944,868],[856,56],[415,376],[444,397],[628,426],[790,45],[304,108],[457,349],[441,161],[515,94],[899,109],[867,195],[718,404],[619,462],[103,33],[862,77],[727,672],[825,815],[722,556],[934,883],[828,322],[630,368],[282,170],[824,371],[851,779],[691,155],[533,382],[884,61],[697,130],[201,105],[798,296],[855,265],[503,31],[388,124],[850,152],[933,203],[736,80],[335,239],[446,6],[630,178],[802,88],[299,270],[696,526],[869,269],[659,292],[284,93],[719,212],[710,480],[497,205],[565,123],[547,442],[582,385],[670,550],[729,218],[731,285],[405,57],[734,683],[424,102],[823,39],[665,629],[392,24],[802,242],[791,620],[864,112],[178,94],[898,511],[978,595],[887,3],[521,144],[515,178],[908,302],[233,60],[735,161],[347,241],[736,117],[233,192],[633,449],[831,806],[308,304],[868,425],[307,33],[907,67],[501,265],[945,62],[516,88],[922,119],[358,150],[969,680],[787,500],[400,366],[662,569],[767,316],[821,38],[945,13],[871,413],[536,251],[647,591],[645,84],[418,242],[153,37],[647,32],[867,298],[667,203],[988,398],[890,578],[988,712],[454,369],[420,92],[644,631],[458,215],[921,153],[913,490],[947,594],[774,121],[286,212],[489,8],[289,236],[809,664],[793,694],[940,395],[647,441],[953,352],[521,194],[924,592],[885,842],[199,149],[489,243],[736,692],[424,329],[788,9],[606,457],[685,615],[405,403],[604,151],[553,430],[876,372],[920,598],[939,666],[993,109],[708,115],[760,153],[753,455],[125,13],[688,153],[883,161],[769,427],[960,308],[824,817],[479,169],[829,163],[773,280],[735,612],[938,610],[914,378],[832,126],[920,715],[653,429],[849,412],[542,103],[668,47],[917,603],[504,271],[760,399],[751,7],[945,327],[46,19],[316,176],[411,38],[666,136],[818,384],[932,108],[972,658],[666,23],[868,518],[690,258],[241,226],[553,535],[837,269],[988,619],[983,285],[635,259],[800,110],[573,65],[841,318],[531,424],[705,77],[474,154],[757,552],[606,18],[871,735],[961,623],[605,13],[900,121],[180,7],[906,737],[862,495],[582,443],[233,197],[629,430],[370,32],[890,864],[879,659],[778,248],[988,434],[521,109],[903,668],[891,809],[529,247],[794,137],[663,648],[988,376],[924,712],[640,319],[409,348],[780,447],[918,327],[570,103],[473,203],[743,469],[445,282],[965,926],[720,359],[862,520],[772,130],[319,192],[703,75],[954,172],[885,208],[629,484],[775,587],[919,260],[835,395],[707,681],[826,105],[991,840],[638,409],[965,125],[949,289],[809,408],[923,423],[853,340],[781,748],[519,0],[317,172],[723,49],[909,580],[780,62],[830,789],[813,784],[903,249],[570,440],[631,625],[720,32],[381,122],[406,112],[865,620],[736,497],[730,280],[417,35],[638,40],[767,531],[679,147],[485,19],[905,554],[897,651],[491,139],[731,722],[627,516],[486,107],[766,184],[793,223],[857,489],[576,156],[878,784],[979,892],[611,501],[964,651],[367,231],[183,59],[905,242],[487,45],[912,534],[623,367],[901,692],[882,816],[407,275],[788,230],[887,286],[652,341],[915,73],[303,45],[960,304],[705,316],[707,314],[920,351],[956,48],[818,814],[529,349],[507,236],[764,206],[911,217],[429,323],[903,487],[642,376],[763,329],[175,66],[823,171],[856,395],[590,106],[384,323],[616,561],[792,785],[887,387],[823,431],[521,418],[161,101],[929,367],[612,352],[859,549],[810,147],[314,13],[920,71],[783,366],[525,399],[300,19],[653,593],[165,99],[772,349],[804,209],[926,156],[335,241],[465,294],[567,502],[365,167],[689,651],[684,403],[584,1],[902,283],[630,311],[743,156],[666,660],[114,90],[542,237],[606,229],[609,206],[514,220],[931,650],[928,398],[892,513],[591,276],[685,406],[185,88],[566,357],[875,495],[798,417],[286,13],[708,410],[748,375],[970,403],[966,910],[943,514],[678,433],[933,876],[489,423],[337,143],[710,491],[932,59],[972,907],[399,174],[396,44],[349,298],[355,230],[719,608],[682,113],[333,172],[930,783],[916,344],[514,92],[614,153],[676,218],[442,425],[556,266],[851,381],[683,247],[285,83],[939,556],[221,35],[546,109],[183,144],[827,506],[737,64],[488,433],[756,294],[842,17],[839,37],[881,256],[689,317],[974,592],[488,225],[603,342],[649,301],[641,478],[904,574],[437,57],[898,59],[509,478],[479,144],[78,16],[231,4],[677,298],[943,58],[632,14],[699,281],[852,308],[251,211],[448,333],[361,289],[837,397],[380,60],[848,340],[981,531],[219,83],[301,112],[993,36],[948,22],[843,830],[858,358],[491,392],[696,45],[983,664],[886,456],[557,521],[919,674],[180,36],[638,291],[951,661],[597,283],[950,881],[515,288],[531,418],[514,499],[254,102],[350,215],[509,25],[610,71],[533,18],[453,42],[157,120],[626,434],[800,671],[900,211],[829,626],[699,269],[415,343],[677,116],[521,82],[568,8],[492,454],[318,197],[645,131],[675,360],[795,563],[254,129],[793,149],[709,512],[591,138],[411,148],[127,25],[154,9],[470,87],[852,660],[739,60],[875,280],[701,332],[288,234],[923,74],[909,362],[870,330],[869,647],[883,338],[711,246],[196,30],[716,393],[811,201],[970,808],[607,398],[755,732],[528,431],[936,237],[633,406],[950,922],[129,53],[904,891],[633,589],[470,129],[432,386],[688,35],[798,663],[319,202],[791,335],[425,63],[937,570],[170,19],[298,262],[714,194],[827,797],[913,824],[584,483],[738,234],[448,161],[942,931],[495,485],[810,683],[885,228],[213,159],[983,716],[611,172],[830,138],[389,332],[970,166],[251,21],[669,555],[439,33],[381,204],[881,724],[843,842],[640,449],[183,32],[384,66],[557,305],[462,424],[841,676],[888,39],[777,511],[994,798],[613,81],[922,574],[442,330],[185,50],[976,48],[428,119],[994,863],[473,182],[786,506],[807,497],[668,276],[308,195],[644,65],[632,188],[673,338],[402,300],[894,336],[420,96],[732,318],[475,402],[969,636],[728,487],[370,163],[648,638],[997,674],[929,386],[341,167],[890,564],[732,368],[711,644],[876,834],[152,150],[139,138],[834,185],[570,185],[966,26],[816,101],[880,642],[602,92],[907,463],[435,367],[405,154],[256,20],[820,36],[411,194],[103,95],[929,59],[648,343],[858,22],[995,335],[836,215],[830,624],[460,326],[802,462],[841,708],[892,273],[784,386],[760,5],[834,602],[963,887],[327,50],[630,112],[809,328],[659,379],[349,84],[485,69],[783,408],[458,128],[976,155],[712,665],[230,28],[526,495],[425,227],[986,182],[299,162],[977,569],[829,258],[603,221],[255,28],[717,519],[924,404],[384,310],[804,552],[880,821],[895,477],[408,285],[236,53],[998,355],[688,13],[834,413],[316,245],[221,169],[951,695],[926,641],[410,266],[574,350],[707,263],[291,79],[953,497],[493,455],[824,623],[289,9],[818,749],[476,284],[529,528],[825,158],[305,152],[447,83],[304,182],[753,6],[879,332],[596,452],[815,665],[28,7],[751,657],[385,208],[985,299],[186,31],[863,176],[421,141],[743,467],[542,21],[900,324],[723,466],[193,62],[397,251],[805,167],[304,284],[622,541],[665,301],[544,17],[702,363],[746,709],[660,389],[461,398],[249,214],[555,533],[422,9],[967,32],[948,125],[566,170],[773,766],[997,54],[958,382],[163,68],[644,396],[603,2],[850,36],[433,292],[962,144],[712,466],[770,170],[992,149],[351,198],[326,127],[760,517],[892,258],[698,522],[920,679],[608,479],[724,163],[664,605],[559,17],[417,343],[822,63],[715,578],[292,16],[346,119],[826,798],[895,567],[325,21],[661,318],[614,152],[666,549],[233,30],[518,403],[766,370],[379,220],[211,62],[403,348],[208,55],[195,131],[879,241],[351,336],[990,10],[849,184],[720,49],[308,129],[439,356],[934,132],[571,210],[952,857],[845,376],[466,34],[343,300],[915,737],[487,78],[912,518],[620,418],[902,827],[887,110],[551,6],[764,14],[60,35],[230,139],[569,540],[521,244],[260,42],[943,523],[955,371],[505,20],[682,157],[582,149],[723,63],[942,461],[504,445],[933,733],[417,80],[626,16],[952,509],[313,65],[419,228],[462,125],[901,712],[759,201],[770,417],[827,672],[763,557],[571,243],[345,279],[873,857],[659,298],[845,140],[287,19],[774,484],[486,301],[648,71],[522,375],[891,618],[866,559],[460,412],[351,267],[881,252],[914,843],[465,400],[416,212],[97,21],[986,376],[137,78],[820,770],[769,274],[615,159],[858,176],[825,346],[321,49],[809,97],[244,16],[684,82],[666,379],[831,492],[805,358],[814,80],[725,142],[384,125],[383,327],[897,707],[575,445],[616,330],[913,463],[659,33],[831,653],[923,635],[618,614],[877,227],[118,68],[858,67],[779,569],[884,203],[832,711],[988,101],[673,96],[507,264],[276,177],[498,281],[763,742],[884,117],[865,312],[950,11],[549,75],[718,626],[732,108],[635,53],[687,529],[703,376],[709,394],[710,595],[821,600],[681,653],[957,265],[876,664],[781,684],[141,111],[904,490],[987,480],[698,134],[924,201],[373,255],[863,320],[709,9],[626,12],[737,512],[967,427],[447,346],[785,240],[721,209],[966,603],[735,49],[559,31],[715,520],[413,64],[623,449],[797,736],[385,93],[491,466],[615,415],[875,168],[727,27],[704,473],[518,106],[483,291],[661,342],[793,248],[585,93],[801,669],[368,303],[517,404],[759,454],[291,147],[680,675],[874,341],[690,288],[852,842],[693,60],[455,396],[459,399],[429,103],[697,210],[714,472],[208,190],[932,929],[316,27],[786,569],[719,502],[690,202],[747,281],[603,573],[470,195],[258,104],[188,74],[715,350],[959,338],[696,81],[822,204],[989,524],[654,339],[555,321],[219,38],[971,327],[581,411],[671,511],[658,46],[439,108],[251,13],[255,102],[979,264],[446,316],[748,243],[571,366],[419,403],[345,50],[972,16],[738,513],[509,359],[461,110],[929,581],[811,585],[518,322],[568,34],[900,49],[845,381],[544,53],[964,576],[949,552],[994,931],[715,462],[299,199],[113,0],[921,518],[751,630],[767,328],[812,106],[910,784],[880,713],[773,720],[971,134],[450,379],[704,146],[379,170],[746,399],[790,113],[391,2],[799,116],[845,193],[909,728],[319,62],[620,172],[528,434],[691,112],[621,588],[974,525],[982,831],[120,111],[970,76],[343,114],[633,64],[935,683],[667,326],[843,399],[973,718],[997,538],[725,282],[511,43],[192,114],[967,856],[185,87],[760,164],[435,18],[678,364],[397,352],[500,47],[949,864],[875,675],[699,583],[644,193],[759,363],[732,367],[850,460],[684,121],[778,131],[785,403],[821,7],[536,275],[577,332],[805,63],[582,75],[736,189],[396,349],[726,473],[964,659],[70,30],[894,206],[760,108],[594,182],[648,452],[931,441],[744,474],[971,868],[655,350],[725,276],[932,596],[759,515],[499,335],[941,535],[767,435],[687,531],[348,325],[389,88],[581,419],[742,665],[495,188],[890,177],[927,674],[711,217],[361,68],[487,407],[525,437],[975,42],[599,122],[909,632],[934,16],[880,165],[178,150],[826,401],[433,119],[174,63],[998,682],[664,571],[997,648],[593,421],[58,53],[292,146],[982,82],[734,682],[357,43],[523,275],[330,282],[797,599],[918,27],[478,50],[929,117],[739,534],[268,148],[439,331],[635,424],[901,465],[748,583],[773,385],[742,598],[554,227],[190,57],[523,10],[542,390],[311,204],[952,72],[499,433],[549,359],[932,502],[743,514],[560,438],[395,223],[594,248],[860,830],[291,179],[575,273],[994,978],[721,325],[683,548],[891,445],[204,135],[979,534],[738,244],[656,572],[534,302],[979,849],[932,829],[763,751],[284,152],[137,104],[415,213],[466,284],[180,21],[959,666],[856,513],[960,888],[733,412],[618,290],[589,463],[531,475],[927,845],[849,179],[735,504],[774,217],[992,580],[144,66],[466,307],[446,324],[674,133],[736,11],[726,373],[608,565],[462,229],[726,351],[382,212],[150,31],[317,298],[405,211],[675,55],[563,342],[501,47],[765,681],[937,129],[965,186],[856,88],[837,326],[558,355],[724,149],[311,104],[481,182],[975,688],[757,640],[834,535],[395,270],[311,5],[717,149],[858,189],[457,146],[647,505],[478,279],[832,308],[286,139],[474,296],[608,482],[366,186],[983,189],[949,256],[919,344],[948,794],[720,251],[755,364],[971,249],[840,512],[859,815],[574,129],[758,281],[907,145],[328,92],[909,583],[990,688],[661,100],[777,188],[277,150],[839,192],[532,507],[834,356],[170,13],[514,211],[277,233],[885,630],[371,245],[985,383],[769,281],[886,135],[896,212],[372,203],[767,312],[713,676],[960,60],[521,50],[627,243],[578,512],[575,326],[47,0],[912,851],[439,192],[777,220],[948,751],[265,235],[963,102],[743,664],[514,218],[994,24],[834,441],[790,300],[679,141],[71,14],[965,87],[801,657],[624,596],[288,86],[533,106],[447,132],[881,223],[889,233],[517,293],[488,89],[284,14],[409,54],[542,221],[293,225],[570,106],[902,641],[937,642],[643,358],[467,73],[741,286],[341,154],[768,138],[440,286],[119,6],[967,451],[917,654],[638,259],[982,76],[501,186],[638,450],[558,164],[932,743],[911,733],[292,74],[962,417],[294,85],[136,103],[395,167],[197,167],[985,682],[865,494],[879,407],[708,419],[692,196],[790,144],[634,500],[718,214],[600,92],[320,213],[286,278],[591,282],[720,565],[606,499],[998,49],[992,316],[719,596],[930,36],[847,583],[256,46],[474,185],[583,114],[856,670],[291,100],[487,235],[739,492],[360,358],[625,239],[792,449],[771,701],[867,598],[866,501],[293,265],[863,115],[783,358],[932,396],[524,282],[125,108],[755,474],[894,566],[581,32],[312,193],[799,670],[967,717],[621,36],[800,428],[599,219],[652,384],[607,136],[825,610],[367,268],[533,7],[772,275],[747,577],[887,124],[888,127],[922,739],[909,744],[498,237],[944,192],[653,28],[587,322],[361,206],[555,313],[533,294],[21,11],[381,340],[710,65],[696,584],[783,558],[235,82],[874,380],[656,125],[972,199],[685,400],[947,450],[949,617],[601,267],[828,278],[459,78],[269,122],[235,75],[563,8],[478,408],[803,8],[868,741],[813,115],[789,370],[837,453],[856,130],[501,356],[687,74],[553,114],[282,174],[123,69],[995,208],[823,241],[150,58],[678,296],[755,524],[833,325],[761,539],[807,600],[613,435],[936,707],[622,132],[802,645],[737,7],[998,142],[283,102],[941,635],[351,287],[922,810],[604,48],[573,55],[340,85],[763,359],[773,44],[270,186],[957,181],[956,764],[895,683],[742,434],[832,30],[623,280],[680,235],[420,298],[814,239],[870,755],[838,464],[234,227],[928,617],[966,4],[835,680],[499,383],[683,507],[895,878],[778,154],[629,596],[875,20],[998,427],[985,318],[590,81],[727,74],[430,212],[867,367],[783,400],[978,526],[836,339],[896,330],[993,896],[152,42],[884,497],[745,134],[835,808],[977,497],[477,464],[847,633],[588,51],[546,384],[807,528],[938,922],[800,75],[915,110],[809,797],[682,622],[747,590],[856,732],[376,45],[719,631],[744,674],[238,0],[424,330],[828,119],[963,754],[686,19],[758,609],[666,366],[761,243],[724,231],[817,801],[971,408],[595,429],[684,67],[110,45],[989,855],[632,178],[858,696],[979,286],[723,51],[280,260],[913,97],[760,601],[468,227],[189,56],[996,187],[664,350],[448,80],[290,204],[935,352],[437,94],[893,498],[451,85],[364,174],[271,198],[917,638],[959,46],[498,239],[761,310],[751,587],[959,284],[518,217],[225,49],[667,133],[576,107],[855,450],[395,393],[676,532],[961,1],[533,210],[861,483],[800,586],[461,52],[908,431],[532,384],[697,188],[674,184],[486,6],[815,22],[782,424],[994,772],[406,194],[441,392],[904,255],[998,867],[966,370],[268,169],[347,153],[709,645],[889,583],[248,102],[752,581],[588,430],[189,102],[760,215],[296,291],[931,87],[619,561],[823,33],[652,535],[340,281],[263,40],[821,471],[865,78],[140,4],[930,258],[733,201],[755,420],[579,198],[895,801],[757,192],[511,215],[481,452],[429,51],[919,313],[580,49]])
	
import cProfile
cProfile.run('test_canFinish()')