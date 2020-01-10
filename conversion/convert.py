def char2ID(c):
	utf8 = int.from_bytes(c.encode("utf-8"), 'big')
	if utf8 >= 0 and utf8 <= 5: return 0 + utf8 - 0
	if utf8 >= 32 and utf8 <= 127: return 6 + utf8 - 32
	if utf8 >= 14909568 and utf8 <= 14909631: return 102 + utf8 - 14909568
	if utf8 >= 14909824 and utf8 <= 14909887: return 166 + utf8 - 14909824
	if utf8 >= 14910080 and utf8 <= 14910143: return 230 + utf8 - 14910080
	if utf8 >= 14910336 and utf8 <= 14910399: return 294 + utf8 - 14910336
	if utf8 >= 14989440 and utf8 <= 14989503: return 358 + utf8 - 14989440
	if utf8 >= 14989696 and utf8 <= 14989759: return 422 + utf8 - 14989696
	if utf8 >= 14989952 and utf8 <= 14990015: return 486 + utf8 - 14989952
	if utf8 >= 14990208 and utf8 <= 14990271: return 550 + utf8 - 14990208
	if utf8 >= 14990464 and utf8 <= 14990527: return 614 + utf8 - 14990464
	if utf8 >= 14990720 and utf8 <= 14990783: return 678 + utf8 - 14990720
	if utf8 >= 14990976 and utf8 <= 14991039: return 742 + utf8 - 14990976
	if utf8 >= 14991232 and utf8 <= 14991295: return 806 + utf8 - 14991232
	if utf8 >= 15040640 and utf8 <= 15040703: return 870 + utf8 - 15040640
	if utf8 >= 15040896 and utf8 <= 15040959: return 934 + utf8 - 15040896
	if utf8 >= 15041152 and utf8 <= 15041215: return 998 + utf8 - 15041152
	if utf8 >= 15041408 and utf8 <= 15041471: return 1062 + utf8 - 15041408
	if utf8 >= 15041664 and utf8 <= 15041727: return 1126 + utf8 - 15041664
	if utf8 >= 15041920 and utf8 <= 15041983: return 1190 + utf8 - 15041920
	if utf8 >= 15042176 and utf8 <= 15042239: return 1254 + utf8 - 15042176
	if utf8 >= 15042432 and utf8 <= 15042495: return 1318 + utf8 - 15042432
	if utf8 >= 15042688 and utf8 <= 15042751: return 1382 + utf8 - 15042688
	if utf8 >= 15042944 and utf8 <= 15043007: return 1446 + utf8 - 15042944
	if utf8 >= 15043200 and utf8 <= 15043263: return 1510 + utf8 - 15043200
	if utf8 >= 15043456 and utf8 <= 15043519: return 1574 + utf8 - 15043456
	if utf8 >= 15043712 and utf8 <= 15043775: return 1638 + utf8 - 15043712
	if utf8 >= 15043968 and utf8 <= 15044031: return 1702 + utf8 - 15043968
	if utf8 >= 15044224 and utf8 <= 15044287: return 1766 + utf8 - 15044224
	if utf8 >= 15044480 and utf8 <= 15044543: return 1830 + utf8 - 15044480
	if utf8 >= 15044736 and utf8 <= 15044799: return 1894 + utf8 - 15044736
	if utf8 >= 15044992 and utf8 <= 15045055: return 1958 + utf8 - 15044992
	if utf8 >= 15045248 and utf8 <= 15045311: return 2022 + utf8 - 15045248
	if utf8 >= 15045504 and utf8 <= 15045567: return 2086 + utf8 - 15045504
	if utf8 >= 15045760 and utf8 <= 15045823: return 2150 + utf8 - 15045760
	if utf8 >= 15046016 and utf8 <= 15046079: return 2214 + utf8 - 15046016
	if utf8 >= 15046272 and utf8 <= 15046335: return 2278 + utf8 - 15046272
	if utf8 >= 15046528 and utf8 <= 15046591: return 2342 + utf8 - 15046528
	if utf8 >= 15046784 and utf8 <= 15046847: return 2406 + utf8 - 15046784
	if utf8 >= 15047040 and utf8 <= 15047103: return 2470 + utf8 - 15047040
	if utf8 >= 15047296 and utf8 <= 15047359: return 2534 + utf8 - 15047296
	if utf8 >= 15047552 and utf8 <= 15047615: return 2598 + utf8 - 15047552
	if utf8 >= 15047808 and utf8 <= 15047871: return 2662 + utf8 - 15047808
	if utf8 >= 15048064 and utf8 <= 15048127: return 2726 + utf8 - 15048064
	if utf8 >= 15048320 and utf8 <= 15048383: return 2790 + utf8 - 15048320
	if utf8 >= 15048576 and utf8 <= 15048639: return 2854 + utf8 - 15048576
	if utf8 >= 15048832 and utf8 <= 15048895: return 2918 + utf8 - 15048832
	if utf8 >= 15049088 and utf8 <= 15049151: return 2982 + utf8 - 15049088
	if utf8 >= 15049344 and utf8 <= 15049407: return 3046 + utf8 - 15049344
	if utf8 >= 15049600 and utf8 <= 15049663: return 3110 + utf8 - 15049600
	if utf8 >= 15049856 and utf8 <= 15049919: return 3174 + utf8 - 15049856
	if utf8 >= 15050112 and utf8 <= 15050175: return 3238 + utf8 - 15050112
	if utf8 >= 15050368 and utf8 <= 15050431: return 3302 + utf8 - 15050368
	if utf8 >= 15050624 and utf8 <= 15050687: return 3366 + utf8 - 15050624
	if utf8 >= 15050880 and utf8 <= 15050943: return 3430 + utf8 - 15050880
	if utf8 >= 15051136 and utf8 <= 15051199: return 3494 + utf8 - 15051136
	if utf8 >= 15051392 and utf8 <= 15051455: return 3558 + utf8 - 15051392
	if utf8 >= 15051648 and utf8 <= 15051711: return 3622 + utf8 - 15051648
	if utf8 >= 15051904 and utf8 <= 15051967: return 3686 + utf8 - 15051904
	if utf8 >= 15052160 and utf8 <= 15052223: return 3750 + utf8 - 15052160
	if utf8 >= 15052416 and utf8 <= 15052479: return 3814 + utf8 - 15052416
	if utf8 >= 15052672 and utf8 <= 15052735: return 3878 + utf8 - 15052672
	if utf8 >= 15052928 and utf8 <= 15052991: return 3942 + utf8 - 15052928
	if utf8 >= 15053184 and utf8 <= 15053247: return 4006 + utf8 - 15053184
	if utf8 >= 15053440 and utf8 <= 15053503: return 4070 + utf8 - 15053440
	if utf8 >= 15053696 and utf8 <= 15053759: return 4134 + utf8 - 15053696
	if utf8 >= 15053952 and utf8 <= 15054015: return 4198 + utf8 - 15053952
	if utf8 >= 15054208 and utf8 <= 15054271: return 4262 + utf8 - 15054208
	if utf8 >= 15054464 and utf8 <= 15054527: return 4326 + utf8 - 15054464
	if utf8 >= 15054720 and utf8 <= 15054783: return 4390 + utf8 - 15054720
	if utf8 >= 15054976 and utf8 <= 15055039: return 4454 + utf8 - 15054976
	if utf8 >= 15055232 and utf8 <= 15055295: return 4518 + utf8 - 15055232
	if utf8 >= 15055488 and utf8 <= 15055551: return 4582 + utf8 - 15055488
	if utf8 >= 15055744 and utf8 <= 15055807: return 4646 + utf8 - 15055744
	if utf8 >= 15056000 and utf8 <= 15056063: return 4710 + utf8 - 15056000
	if utf8 >= 15056256 and utf8 <= 15056319: return 4774 + utf8 - 15056256
	if utf8 >= 15056512 and utf8 <= 15056575: return 4838 + utf8 - 15056512
	if utf8 >= 15056768 and utf8 <= 15056831: return 4902 + utf8 - 15056768
	if utf8 >= 15106176 and utf8 <= 15106239: return 4966 + utf8 - 15106176
	if utf8 >= 15106432 and utf8 <= 15106495: return 5030 + utf8 - 15106432
	if utf8 >= 15106688 and utf8 <= 15106751: return 5094 + utf8 - 15106688
	if utf8 >= 15106944 and utf8 <= 15107007: return 5158 + utf8 - 15106944
	if utf8 >= 15107200 and utf8 <= 15107263: return 5222 + utf8 - 15107200
	if utf8 >= 15107456 and utf8 <= 15107519: return 5286 + utf8 - 15107456
	if utf8 >= 15107712 and utf8 <= 15107775: return 5350 + utf8 - 15107712
	if utf8 >= 15107968 and utf8 <= 15108031: return 5414 + utf8 - 15107968
	if utf8 >= 15108224 and utf8 <= 15108287: return 5478 + utf8 - 15108224
	if utf8 >= 15108480 and utf8 <= 15108543: return 5542 + utf8 - 15108480
	if utf8 >= 15108736 and utf8 <= 15108799: return 5606 + utf8 - 15108736
	if utf8 >= 15108992 and utf8 <= 15109055: return 5670 + utf8 - 15108992
	if utf8 >= 15109248 and utf8 <= 15109311: return 5734 + utf8 - 15109248
	if utf8 >= 15109504 and utf8 <= 15109567: return 5798 + utf8 - 15109504
	if utf8 >= 15109760 and utf8 <= 15109823: return 5862 + utf8 - 15109760
	if utf8 >= 15110016 and utf8 <= 15110079: return 5926 + utf8 - 15110016
	if utf8 >= 15110272 and utf8 <= 15110335: return 5990 + utf8 - 15110272
	if utf8 >= 15110528 and utf8 <= 15110591: return 6054 + utf8 - 15110528
	if utf8 >= 15110784 and utf8 <= 15110847: return 6118 + utf8 - 15110784
	if utf8 >= 15111040 and utf8 <= 15111103: return 6182 + utf8 - 15111040
	if utf8 >= 15111296 and utf8 <= 15111359: return 6246 + utf8 - 15111296
	if utf8 >= 15111552 and utf8 <= 15111615: return 6310 + utf8 - 15111552
	if utf8 >= 15111808 and utf8 <= 15111871: return 6374 + utf8 - 15111808
	if utf8 >= 15112064 and utf8 <= 15112127: return 6438 + utf8 - 15112064
	if utf8 >= 15112320 and utf8 <= 15112383: return 6502 + utf8 - 15112320
	if utf8 >= 15112576 and utf8 <= 15112639: return 6566 + utf8 - 15112576
	if utf8 >= 15112832 and utf8 <= 15112895: return 6630 + utf8 - 15112832
	if utf8 >= 15113088 and utf8 <= 15113151: return 6694 + utf8 - 15113088
	if utf8 >= 15113344 and utf8 <= 15113407: return 6758 + utf8 - 15113344
	if utf8 >= 15113600 and utf8 <= 15113663: return 6822 + utf8 - 15113600
	if utf8 >= 15113856 and utf8 <= 15113919: return 6886 + utf8 - 15113856
	if utf8 >= 15114112 and utf8 <= 15114175: return 6950 + utf8 - 15114112
	if utf8 >= 15114368 and utf8 <= 15114431: return 7014 + utf8 - 15114368
	if utf8 >= 15114624 and utf8 <= 15114687: return 7078 + utf8 - 15114624
	if utf8 >= 15114880 and utf8 <= 15114943: return 7142 + utf8 - 15114880
	if utf8 >= 15115136 and utf8 <= 15115199: return 7206 + utf8 - 15115136
	if utf8 >= 15115392 and utf8 <= 15115455: return 7270 + utf8 - 15115392
	if utf8 >= 15115648 and utf8 <= 15115711: return 7334 + utf8 - 15115648
	if utf8 >= 15115904 and utf8 <= 15115967: return 7398 + utf8 - 15115904
	if utf8 >= 15116160 and utf8 <= 15116223: return 7462 + utf8 - 15116160
	if utf8 >= 15116416 and utf8 <= 15116479: return 7526 + utf8 - 15116416
	if utf8 >= 15116672 and utf8 <= 15116735: return 7590 + utf8 - 15116672
	if utf8 >= 15116928 and utf8 <= 15116991: return 7654 + utf8 - 15116928
	if utf8 >= 15117184 and utf8 <= 15117247: return 7718 + utf8 - 15117184
	if utf8 >= 15117440 and utf8 <= 15117503: return 7782 + utf8 - 15117440
	if utf8 >= 15117696 and utf8 <= 15117759: return 7846 + utf8 - 15117696
	if utf8 >= 15117952 and utf8 <= 15118015: return 7910 + utf8 - 15117952
	if utf8 >= 15118208 and utf8 <= 15118271: return 7974 + utf8 - 15118208
	if utf8 >= 15118464 and utf8 <= 15118527: return 8038 + utf8 - 15118464
	if utf8 >= 15118720 and utf8 <= 15118783: return 8102 + utf8 - 15118720
	if utf8 >= 15118976 and utf8 <= 15119039: return 8166 + utf8 - 15118976
	if utf8 >= 15119232 and utf8 <= 15119295: return 8230 + utf8 - 15119232
	if utf8 >= 15119488 and utf8 <= 15119551: return 8294 + utf8 - 15119488
	if utf8 >= 15119744 and utf8 <= 15119807: return 8358 + utf8 - 15119744
	if utf8 >= 15120000 and utf8 <= 15120063: return 8422 + utf8 - 15120000
	if utf8 >= 15120256 and utf8 <= 15120319: return 8486 + utf8 - 15120256
	if utf8 >= 15120512 and utf8 <= 15120575: return 8550 + utf8 - 15120512
	if utf8 >= 15120768 and utf8 <= 15120831: return 8614 + utf8 - 15120768
	if utf8 >= 15121024 and utf8 <= 15121087: return 8678 + utf8 - 15121024
	if utf8 >= 15121280 and utf8 <= 15121343: return 8742 + utf8 - 15121280
	if utf8 >= 15121536 and utf8 <= 15121599: return 8806 + utf8 - 15121536
	if utf8 >= 15121792 and utf8 <= 15121855: return 8870 + utf8 - 15121792
	if utf8 >= 15122048 and utf8 <= 15122111: return 8934 + utf8 - 15122048
	if utf8 >= 15122304 and utf8 <= 15122367: return 8998 + utf8 - 15122304
	if utf8 >= 15171712 and utf8 <= 15171775: return 9062 + utf8 - 15171712
	if utf8 >= 15171968 and utf8 <= 15172031: return 9126 + utf8 - 15171968
	if utf8 >= 15172224 and utf8 <= 15172287: return 9190 + utf8 - 15172224
	if utf8 >= 15172480 and utf8 <= 15172543: return 9254 + utf8 - 15172480
	if utf8 >= 15172736 and utf8 <= 15172799: return 9318 + utf8 - 15172736
	if utf8 >= 15172992 and utf8 <= 15173055: return 9382 + utf8 - 15172992
	if utf8 >= 15173248 and utf8 <= 15173311: return 9446 + utf8 - 15173248
	if utf8 >= 15173504 and utf8 <= 15173567: return 9510 + utf8 - 15173504
	if utf8 >= 15173760 and utf8 <= 15173823: return 9574 + utf8 - 15173760
	if utf8 >= 15174016 and utf8 <= 15174079: return 9638 + utf8 - 15174016
	if utf8 >= 15174272 and utf8 <= 15174335: return 9702 + utf8 - 15174272
	if utf8 >= 15174528 and utf8 <= 15174591: return 9766 + utf8 - 15174528
	if utf8 >= 15174784 and utf8 <= 15174847: return 9830 + utf8 - 15174784
	if utf8 >= 15175040 and utf8 <= 15175103: return 9894 + utf8 - 15175040
	if utf8 >= 15175296 and utf8 <= 15175359: return 9958 + utf8 - 15175296
	if utf8 >= 15175552 and utf8 <= 15175615: return 10022 + utf8 - 15175552
	if utf8 >= 15175808 and utf8 <= 15175871: return 10086 + utf8 - 15175808
	if utf8 >= 15176064 and utf8 <= 15176127: return 10150 + utf8 - 15176064
	if utf8 >= 15176320 and utf8 <= 15176383: return 10214 + utf8 - 15176320
	if utf8 >= 15176576 and utf8 <= 15176639: return 10278 + utf8 - 15176576
	if utf8 >= 15176832 and utf8 <= 15176895: return 10342 + utf8 - 15176832
	if utf8 >= 15177088 and utf8 <= 15177151: return 10406 + utf8 - 15177088
	if utf8 >= 15177344 and utf8 <= 15177407: return 10470 + utf8 - 15177344
	if utf8 >= 15177600 and utf8 <= 15177663: return 10534 + utf8 - 15177600
	if utf8 >= 15177856 and utf8 <= 15177919: return 10598 + utf8 - 15177856
	if utf8 >= 15178112 and utf8 <= 15178175: return 10662 + utf8 - 15178112
	if utf8 >= 15178368 and utf8 <= 15178431: return 10726 + utf8 - 15178368
	if utf8 >= 15178624 and utf8 <= 15178687: return 10790 + utf8 - 15178624
	if utf8 >= 15178880 and utf8 <= 15178943: return 10854 + utf8 - 15178880
	if utf8 >= 15179136 and utf8 <= 15179199: return 10918 + utf8 - 15179136
	if utf8 >= 15179392 and utf8 <= 15179455: return 10982 + utf8 - 15179392
	if utf8 >= 15179648 and utf8 <= 15179711: return 11046 + utf8 - 15179648
	if utf8 >= 15179904 and utf8 <= 15179967: return 11110 + utf8 - 15179904
	if utf8 >= 15180160 and utf8 <= 15180223: return 11174 + utf8 - 15180160
	if utf8 >= 15180416 and utf8 <= 15180479: return 11238 + utf8 - 15180416
	if utf8 >= 15180672 and utf8 <= 15180735: return 11302 + utf8 - 15180672
	if utf8 >= 15180928 and utf8 <= 15180991: return 11366 + utf8 - 15180928
	if utf8 >= 15181184 and utf8 <= 15181247: return 11430 + utf8 - 15181184
	if utf8 >= 15181440 and utf8 <= 15181503: return 11494 + utf8 - 15181440
	if utf8 >= 15181696 and utf8 <= 15181759: return 11558 + utf8 - 15181696
	if utf8 >= 15181952 and utf8 <= 15182015: return 11622 + utf8 - 15181952
	if utf8 >= 15182208 and utf8 <= 15182271: return 11686 + utf8 - 15182208
	if utf8 >= 15182464 and utf8 <= 15182527: return 11750 + utf8 - 15182464
	if utf8 >= 15182720 and utf8 <= 15182783: return 11814 + utf8 - 15182720
	if utf8 >= 15182976 and utf8 <= 15183039: return 11878 + utf8 - 15182976
	if utf8 >= 15183232 and utf8 <= 15183295: return 11942 + utf8 - 15183232
	if utf8 >= 15183488 and utf8 <= 15183551: return 12006 + utf8 - 15183488
	if utf8 >= 15183744 and utf8 <= 15183807: return 12070 + utf8 - 15183744
	if utf8 >= 15184000 and utf8 <= 15184063: return 12134 + utf8 - 15184000
	if utf8 >= 15184256 and utf8 <= 15184319: return 12198 + utf8 - 15184256
	if utf8 >= 15184512 and utf8 <= 15184575: return 12262 + utf8 - 15184512
	if utf8 >= 15184768 and utf8 <= 15184831: return 12326 + utf8 - 15184768
	if utf8 >= 15185024 and utf8 <= 15185087: return 12390 + utf8 - 15185024
	if utf8 >= 15185280 and utf8 <= 15185343: return 12454 + utf8 - 15185280
	if utf8 >= 15185536 and utf8 <= 15185599: return 12518 + utf8 - 15185536
	if utf8 >= 15185792 and utf8 <= 15185855: return 12582 + utf8 - 15185792
	if utf8 >= 15186048 and utf8 <= 15186111: return 12646 + utf8 - 15186048
	if utf8 >= 15186304 and utf8 <= 15186367: return 12710 + utf8 - 15186304
	if utf8 >= 15186560 and utf8 <= 15186623: return 12774 + utf8 - 15186560
	if utf8 >= 15186816 and utf8 <= 15186879: return 12838 + utf8 - 15186816
	if utf8 >= 15187072 and utf8 <= 15187135: return 12902 + utf8 - 15187072
	if utf8 >= 15187328 and utf8 <= 15187391: return 12966 + utf8 - 15187328
	if utf8 >= 15187584 and utf8 <= 15187647: return 13030 + utf8 - 15187584
	if utf8 >= 15187840 and utf8 <= 15187903: return 13094 + utf8 - 15187840
	if utf8 >= 15237248 and utf8 <= 15237311: return 13158 + utf8 - 15237248
	if utf8 >= 15237504 and utf8 <= 15237567: return 13222 + utf8 - 15237504
	if utf8 >= 15237760 and utf8 <= 15237823: return 13286 + utf8 - 15237760
	if utf8 >= 15238016 and utf8 <= 15238079: return 13350 + utf8 - 15238016
	if utf8 >= 15238272 and utf8 <= 15238335: return 13414 + utf8 - 15238272
	if utf8 >= 15238528 and utf8 <= 15238591: return 13478 + utf8 - 15238528
	if utf8 >= 15238784 and utf8 <= 15238847: return 13542 + utf8 - 15238784
	if utf8 >= 15239040 and utf8 <= 15239103: return 13606 + utf8 - 15239040
	if utf8 >= 15239296 and utf8 <= 15239359: return 13670 + utf8 - 15239296
	if utf8 >= 15239552 and utf8 <= 15239615: return 13734 + utf8 - 15239552
	if utf8 >= 15239808 and utf8 <= 15239871: return 13798 + utf8 - 15239808
	if utf8 >= 15240064 and utf8 <= 15240127: return 13862 + utf8 - 15240064
	if utf8 >= 15240320 and utf8 <= 15240383: return 13926 + utf8 - 15240320
	if utf8 >= 15240576 and utf8 <= 15240639: return 13990 + utf8 - 15240576
	if utf8 >= 15240832 and utf8 <= 15240895: return 14054 + utf8 - 15240832
	if utf8 >= 15241088 and utf8 <= 15241151: return 14118 + utf8 - 15241088
	if utf8 >= 15241344 and utf8 <= 15241407: return 14182 + utf8 - 15241344
	if utf8 >= 15241600 and utf8 <= 15241663: return 14246 + utf8 - 15241600
	if utf8 >= 15241856 and utf8 <= 15241919: return 14310 + utf8 - 15241856
	if utf8 >= 15242112 and utf8 <= 15242175: return 14374 + utf8 - 15242112
	if utf8 >= 15242368 and utf8 <= 15242431: return 14438 + utf8 - 15242368
	if utf8 >= 15242624 and utf8 <= 15242687: return 14502 + utf8 - 15242624
	if utf8 >= 15242880 and utf8 <= 15242943: return 14566 + utf8 - 15242880
	if utf8 >= 15243136 and utf8 <= 15243199: return 14630 + utf8 - 15243136
	if utf8 >= 15243392 and utf8 <= 15243455: return 14694 + utf8 - 15243392
	if utf8 >= 15243648 and utf8 <= 15243711: return 14758 + utf8 - 15243648
	if utf8 >= 15243904 and utf8 <= 15243967: return 14822 + utf8 - 15243904
	if utf8 >= 15244160 and utf8 <= 15244223: return 14886 + utf8 - 15244160
	if utf8 >= 15244416 and utf8 <= 15244479: return 14950 + utf8 - 15244416
	if utf8 >= 15244672 and utf8 <= 15244735: return 15014 + utf8 - 15244672
	if utf8 >= 15244928 and utf8 <= 15244991: return 15078 + utf8 - 15244928
	if utf8 >= 15245184 and utf8 <= 15245247: return 15142 + utf8 - 15245184
	if utf8 >= 15245440 and utf8 <= 15245503: return 15206 + utf8 - 15245440
	if utf8 >= 15245696 and utf8 <= 15245759: return 15270 + utf8 - 15245696
	if utf8 >= 15245952 and utf8 <= 15246015: return 15334 + utf8 - 15245952
	if utf8 >= 15246208 and utf8 <= 15246271: return 15398 + utf8 - 15246208
	if utf8 >= 15246464 and utf8 <= 15246527: return 15462 + utf8 - 15246464
	if utf8 >= 15246720 and utf8 <= 15246783: return 15526 + utf8 - 15246720
	if utf8 >= 15246976 and utf8 <= 15247039: return 15590 + utf8 - 15246976
	if utf8 >= 15247232 and utf8 <= 15247295: return 15654 + utf8 - 15247232
	if utf8 >= 15247488 and utf8 <= 15247551: return 15718 + utf8 - 15247488
	if utf8 >= 15247744 and utf8 <= 15247807: return 15782 + utf8 - 15247744
	if utf8 >= 15248000 and utf8 <= 15248063: return 15846 + utf8 - 15248000
	if utf8 >= 15248256 and utf8 <= 15248319: return 15910 + utf8 - 15248256
	if utf8 >= 15248512 and utf8 <= 15248575: return 15974 + utf8 - 15248512
	if utf8 >= 15248768 and utf8 <= 15248831: return 16038 + utf8 - 15248768
	if utf8 >= 15249024 and utf8 <= 15249087: return 16102 + utf8 - 15249024
	if utf8 >= 15249280 and utf8 <= 15249343: return 16166 + utf8 - 15249280
	if utf8 >= 15249536 and utf8 <= 15249599: return 16230 + utf8 - 15249536
	if utf8 >= 15249792 and utf8 <= 15249855: return 16294 + utf8 - 15249792
	if utf8 >= 15250048 and utf8 <= 15250111: return 16358 + utf8 - 15250048
	if utf8 >= 15250304 and utf8 <= 15250367: return 16422 + utf8 - 15250304
	if utf8 >= 15250560 and utf8 <= 15250623: return 16486 + utf8 - 15250560
	if utf8 >= 15250816 and utf8 <= 15250879: return 16550 + utf8 - 15250816
	if utf8 >= 15251072 and utf8 <= 15251135: return 16614 + utf8 - 15251072
	if utf8 >= 15251328 and utf8 <= 15251391: return 16678 + utf8 - 15251328
	if utf8 >= 15251584 and utf8 <= 15251647: return 16742 + utf8 - 15251584
	if utf8 >= 15251840 and utf8 <= 15251903: return 16806 + utf8 - 15251840
	if utf8 >= 15252096 and utf8 <= 15252159: return 16870 + utf8 - 15252096
	if utf8 >= 15252352 and utf8 <= 15252415: return 16934 + utf8 - 15252352
	if utf8 >= 15252608 and utf8 <= 15252671: return 16998 + utf8 - 15252608
	if utf8 >= 15252864 and utf8 <= 15252927: return 17062 + utf8 - 15252864
	if utf8 >= 15253120 and utf8 <= 15253183: return 17126 + utf8 - 15253120
	if utf8 >= 15253376 and utf8 <= 15253439: return 17190 + utf8 - 15253376
	if utf8 >= 15302784 and utf8 <= 15302847: return 17254 + utf8 - 15302784
	if utf8 >= 15303040 and utf8 <= 15303103: return 17318 + utf8 - 15303040
	if utf8 >= 15303296 and utf8 <= 15303359: return 17382 + utf8 - 15303296
	if utf8 >= 15303552 and utf8 <= 15303615: return 17446 + utf8 - 15303552
	if utf8 >= 15303808 and utf8 <= 15303871: return 17510 + utf8 - 15303808
	if utf8 >= 15304064 and utf8 <= 15304127: return 17574 + utf8 - 15304064
	if utf8 >= 15304320 and utf8 <= 15304383: return 17638 + utf8 - 15304320
	if utf8 >= 15304576 and utf8 <= 15304639: return 17702 + utf8 - 15304576
	if utf8 >= 15304832 and utf8 <= 15304895: return 17766 + utf8 - 15304832
	if utf8 >= 15305088 and utf8 <= 15305151: return 17830 + utf8 - 15305088
	if utf8 >= 15305344 and utf8 <= 15305407: return 17894 + utf8 - 15305344
	if utf8 >= 15305600 and utf8 <= 15305663: return 17958 + utf8 - 15305600
	if utf8 >= 15305856 and utf8 <= 15305919: return 18022 + utf8 - 15305856
	if utf8 >= 15306112 and utf8 <= 15306175: return 18086 + utf8 - 15306112
	if utf8 >= 15306368 and utf8 <= 15306431: return 18150 + utf8 - 15306368
	if utf8 >= 15306624 and utf8 <= 15306687: return 18214 + utf8 - 15306624
	if utf8 >= 15306880 and utf8 <= 15306943: return 18278 + utf8 - 15306880
	if utf8 >= 15307136 and utf8 <= 15307199: return 18342 + utf8 - 15307136
	if utf8 >= 15307392 and utf8 <= 15307455: return 18406 + utf8 - 15307392
	if utf8 >= 15307648 and utf8 <= 15307711: return 18470 + utf8 - 15307648
	if utf8 >= 15307904 and utf8 <= 15307967: return 18534 + utf8 - 15307904
	if utf8 >= 15308160 and utf8 <= 15308223: return 18598 + utf8 - 15308160
	if utf8 >= 15308416 and utf8 <= 15308479: return 18662 + utf8 - 15308416
	if utf8 >= 15308672 and utf8 <= 15308735: return 18726 + utf8 - 15308672
	if utf8 >= 15308928 and utf8 <= 15308991: return 18790 + utf8 - 15308928
	if utf8 >= 15309184 and utf8 <= 15309247: return 18854 + utf8 - 15309184
	if utf8 >= 15309440 and utf8 <= 15309503: return 18918 + utf8 - 15309440
	if utf8 >= 15309696 and utf8 <= 15309759: return 18982 + utf8 - 15309696
	if utf8 >= 15309952 and utf8 <= 15310015: return 19046 + utf8 - 15309952
	if utf8 >= 15310208 and utf8 <= 15310271: return 19110 + utf8 - 15310208
	if utf8 >= 15310464 and utf8 <= 15310527: return 19174 + utf8 - 15310464
	if utf8 >= 15310720 and utf8 <= 15310783: return 19238 + utf8 - 15310720
	if utf8 >= 15310976 and utf8 <= 15311039: return 19302 + utf8 - 15310976
	if utf8 >= 15311232 and utf8 <= 15311295: return 19366 + utf8 - 15311232
	if utf8 >= 15311488 and utf8 <= 15311551: return 19430 + utf8 - 15311488
	if utf8 >= 15311744 and utf8 <= 15311807: return 19494 + utf8 - 15311744
	if utf8 >= 15312000 and utf8 <= 15312063: return 19558 + utf8 - 15312000
	if utf8 >= 15312256 and utf8 <= 15312319: return 19622 + utf8 - 15312256
	if utf8 >= 15312512 and utf8 <= 15312575: return 19686 + utf8 - 15312512
	if utf8 >= 15312768 and utf8 <= 15312831: return 19750 + utf8 - 15312768
	if utf8 >= 15313024 and utf8 <= 15313087: return 19814 + utf8 - 15313024
	if utf8 >= 15313280 and utf8 <= 15313343: return 19878 + utf8 - 15313280
	if utf8 >= 15313536 and utf8 <= 15313599: return 19942 + utf8 - 15313536
	if utf8 >= 15313792 and utf8 <= 15313855: return 20006 + utf8 - 15313792
	if utf8 >= 15314048 and utf8 <= 15314111: return 20070 + utf8 - 15314048
	if utf8 >= 15314304 and utf8 <= 15314367: return 20134 + utf8 - 15314304
	if utf8 >= 15314560 and utf8 <= 15314623: return 20198 + utf8 - 15314560
	if utf8 >= 15314816 and utf8 <= 15314879: return 20262 + utf8 - 15314816
	if utf8 >= 15315072 and utf8 <= 15315135: return 20326 + utf8 - 15315072
	if utf8 >= 15315328 and utf8 <= 15315391: return 20390 + utf8 - 15315328
	if utf8 >= 15315584 and utf8 <= 15315647: return 20454 + utf8 - 15315584
	if utf8 >= 15315840 and utf8 <= 15315903: return 20518 + utf8 - 15315840
	if utf8 >= 15316096 and utf8 <= 15316159: return 20582 + utf8 - 15316096
	if utf8 >= 15316352 and utf8 <= 15316415: return 20646 + utf8 - 15316352
	if utf8 >= 15316608 and utf8 <= 15316671: return 20710 + utf8 - 15316608
	if utf8 >= 15316864 and utf8 <= 15316927: return 20774 + utf8 - 15316864
	if utf8 >= 15317120 and utf8 <= 15317183: return 20838 + utf8 - 15317120
	if utf8 >= 15317376 and utf8 <= 15317439: return 20902 + utf8 - 15317376
	if utf8 >= 15317632 and utf8 <= 15317695: return 20966 + utf8 - 15317632
	if utf8 >= 15317888 and utf8 <= 15317951: return 21030 + utf8 - 15317888
	if utf8 >= 15318144 and utf8 <= 15318207: return 21094 + utf8 - 15318144
	if utf8 >= 15318400 and utf8 <= 15318463: return 21158 + utf8 - 15318400
	if utf8 >= 15318656 and utf8 <= 15318719: return 21222 + utf8 - 15318656
	if utf8 >= 15318912 and utf8 <= 15318975: return 21286 + utf8 - 15318912
	if utf8 >= 15711360 and utf8 <= 15711423: return 21350 + utf8 - 15711360
	if utf8 >= 15711616 and utf8 <= 15711679: return 21414 + utf8 - 15711616
	if utf8 >= 15711872 and utf8 <= 15711903: return 21478 + utf8 - 15711872
	if utf8 >= 14844032 and utf8 <= 14844095: return 21510 + utf8 - 14844032
	if utf8 >= 14844288 and utf8 <= 14844351: return 21574 + utf8 - 14844288
	if utf8 == 14849152: return 21638
	if utf8 >= 14850464 and utf8 <= 14850479: return 21639 + utf8 - 14850464
	if utf8 >= 14850176 and utf8 <= 14850191: return 21655 + utf8 - 14850176
	if utf8 >= 49824 and utf8 <= 49855: return 21671 + utf8 - 49824
	if utf8 >= 50048 and utf8 <= 50095: return 21703 + utf8 - 50048
	if utf8 >= 50304 and utf8 <= 50351: return 21751 + utf8 - 50304
	if utf8 >= 50560 and utf8 <= 50607: return 21799 + utf8 - 50560
	if utf8 >= 50816 and utf8 <= 50863: return 21847 + utf8 - 50816
	if utf8 >= 51072 and utf8 <= 51119: return 21895 + utf8 - 51072
	if utf8 >= 51328 and utf8 <= 51375: return 21943 + utf8 - 51328
	if utf8 >= 51584 and utf8 <= 51631: return 21991 + utf8 - 51584
	if utf8 >= 51840 and utf8 <= 51887: return 22039 + utf8 - 51840
	if utf8 >= 52096 and utf8 <= 52143: return 22087 + utf8 - 52096
	if utf8 >= 52352 and utf8 <= 52399: return 22135 + utf8 - 52352
	if utf8 >= 52608 and utf8 <= 52655: return 22183 + utf8 - 52608
	if utf8 >= 52864 and utf8 <= 52927: return 22231 + utf8 - 52864
	if utf8 >= 53120 and utf8 <= 53183: return 22295 + utf8 - 53120
	if utf8 >= 53376 and utf8 <= 53439: return 22359 + utf8 - 53376
	if utf8 >= 53632 and utf8 <= 53695: return 22423 + utf8 - 53632
	if utf8 >= 53888 and utf8 <= 53951: return 22487 + utf8 - 53888
	if utf8 >= 54144 and utf8 <= 54207: return 22551 + utf8 - 54144
	if utf8 >= 54400 and utf8 <= 54463: return 22615 + utf8 - 54400
	if utf8 >= 54656 and utf8 <= 54719: return 22679 + utf8 - 54656
	if utf8 >= 54912 and utf8 <= 54975: return 22743 + utf8 - 54912
	if utf8 >= 55168 and utf8 <= 55231: return 22807 + utf8 - 55168
	if utf8 >= 55424 and utf8 <= 55487: return 22871 + utf8 - 55424
	if utf8 >= 55680 and utf8 <= 55743: return 22935 + utf8 - 55680
	if utf8 >= 55936 and utf8 <= 55999: return 22999 + utf8 - 55936
	if utf8 >= 56192 and utf8 <= 56255: return 23063 + utf8 - 56192
	if utf8 >= 15710608 and utf8 <= 15710639: return 23127 + utf8 - 15710608
	if utf8 >= 14845312 and utf8 <= 14845375: return 23159 + utf8 - 14845312
	if utf8 >= 14845568 and utf8 <= 14845631: return 23223 + utf8 - 14845568
	if utf8 >= 14845824 and utf8 <= 14845887: return 23287 + utf8 - 14845824
	if utf8 >= 14846080 and utf8 <= 14846143: return 23351 + utf8 - 14846080
	if utf8 >= 14846336 and utf8 <= 14846399: return 23415 + utf8 - 14846336
	if utf8 >= 14846592 and utf8 <= 14846655: return 23479 + utf8 - 14846592
	if utf8 >= 14846848 and utf8 <= 14846911: return 23543 + utf8 - 14846848
	if utf8 >= 14847104 and utf8 <= 14847167: return 23607 + utf8 - 14847104
	if utf8 >= 14847360 and utf8 <= 14847423: return 23671 + utf8 - 14847360
	if utf8 >= 14847616 and utf8 <= 14847679: return 23735 + utf8 - 14847616
	if utf8 >= 14847872 and utf8 <= 14847935: return 23799 + utf8 - 14847872
	if utf8 >= 14848384 and utf8 <= 14848447: return 23863 + utf8 - 14848384
	if utf8 >= 14848640 and utf8 <= 14848703: return 23927 + utf8 - 14848640
	if utf8 >= 14848896 and utf8 <= 14848959: return 23991 + utf8 - 14848896
	if utf8 >= 14912640 and utf8 <= 14912703: return 24055 + utf8 - 14912640
	if utf8 >= 14912896 and utf8 <= 14912959: return 24119 + utf8 - 14912896
	if utf8 >= 14913152 and utf8 <= 14913215: return 24183 + utf8 - 14913152
	if utf8 >= 14913408 and utf8 <= 14913471: return 24247 + utf8 - 14913408
	if utf8 >= 14845056 and utf8 <= 14845119: return 24311 + utf8 - 14845056
	if utf8 >= 14849696 and utf8 <= 14849727: return 24375 + utf8 - 14849696
	if utf8 >= 14849920 and utf8 <= 14849983: return 24407 + utf8 - 14849920
	if utf8 == 14851229: return 24471
	if utf8 == 14851228: return 24472
	if utf8 == 14851492: return 24473
	if utf8 == 15710350: return 24474
	if utf8 == 15710351: return 24475
	if utf8 == 14849153: return 24476
	if utf8 == 15712163: return 24477
	if utf8 == 14850963: return 24478
	if utf8 == 14849160: return 24479
	if utf8 == 14851263: return 24480
	if utf8 == 14850432: return 24481
	if utf8 == 14851745: return 24482
	if utf8 == 14849157: return 24483
	if utf8 == 14850434: return 24484
	if utf8 == 14850730: return 24485
	if utf8 == 14849155: return 24486
	if utf8 == 15712165: return 24487
	if utf8 == 14849164: return 24488
	if utf8 == 14849168: return 24489
	if utf8 == 14727569: return 24490
	if utf8 == 14849672: return 24491
	if utf8 == 14851221: return 24492
	if utf8 == 50103: return 24493
	if utf8 == 14849154: return 24494
	if utf8 == 14849167: return 24495
	if utf8 == 14851239: return 24496
	if utf8 == 14850195: return 24497
	return 2
def ID2char(id):
	if id >= 0 and id < 5: return id
	if id >= 6 and id <= 101: return (32 + id - 6).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 102 and id <= 165: return (14909568 + id - 102).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 166 and id <= 229: return (14909824 + id - 166).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 230 and id <= 293: return (14910080 + id - 230).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 294 and id <= 357: return (14910336 + id - 294).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 358 and id <= 421: return (14989440 + id - 358).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 422 and id <= 485: return (14989696 + id - 422).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 486 and id <= 549: return (14989952 + id - 486).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 550 and id <= 613: return (14990208 + id - 550).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 614 and id <= 677: return (14990464 + id - 614).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 678 and id <= 741: return (14990720 + id - 678).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 742 and id <= 805: return (14990976 + id - 742).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 806 and id <= 869: return (14991232 + id - 806).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 870 and id <= 933: return (15040640 + id - 870).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 934 and id <= 997: return (15040896 + id - 934).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 998 and id <= 1061: return (15041152 + id - 998).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1062 and id <= 1125: return (15041408 + id - 1062).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1126 and id <= 1189: return (15041664 + id - 1126).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1190 and id <= 1253: return (15041920 + id - 1190).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1254 and id <= 1317: return (15042176 + id - 1254).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1318 and id <= 1381: return (15042432 + id - 1318).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1382 and id <= 1445: return (15042688 + id - 1382).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1446 and id <= 1509: return (15042944 + id - 1446).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1510 and id <= 1573: return (15043200 + id - 1510).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1574 and id <= 1637: return (15043456 + id - 1574).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1638 and id <= 1701: return (15043712 + id - 1638).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1702 and id <= 1765: return (15043968 + id - 1702).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1766 and id <= 1829: return (15044224 + id - 1766).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1830 and id <= 1893: return (15044480 + id - 1830).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1894 and id <= 1957: return (15044736 + id - 1894).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 1958 and id <= 2021: return (15044992 + id - 1958).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2022 and id <= 2085: return (15045248 + id - 2022).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2086 and id <= 2149: return (15045504 + id - 2086).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2150 and id <= 2213: return (15045760 + id - 2150).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2214 and id <= 2277: return (15046016 + id - 2214).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2278 and id <= 2341: return (15046272 + id - 2278).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2342 and id <= 2405: return (15046528 + id - 2342).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2406 and id <= 2469: return (15046784 + id - 2406).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2470 and id <= 2533: return (15047040 + id - 2470).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2534 and id <= 2597: return (15047296 + id - 2534).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2598 and id <= 2661: return (15047552 + id - 2598).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2662 and id <= 2725: return (15047808 + id - 2662).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2726 and id <= 2789: return (15048064 + id - 2726).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2790 and id <= 2853: return (15048320 + id - 2790).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2854 and id <= 2917: return (15048576 + id - 2854).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2918 and id <= 2981: return (15048832 + id - 2918).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 2982 and id <= 3045: return (15049088 + id - 2982).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3046 and id <= 3109: return (15049344 + id - 3046).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3110 and id <= 3173: return (15049600 + id - 3110).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3174 and id <= 3237: return (15049856 + id - 3174).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3238 and id <= 3301: return (15050112 + id - 3238).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3302 and id <= 3365: return (15050368 + id - 3302).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3366 and id <= 3429: return (15050624 + id - 3366).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3430 and id <= 3493: return (15050880 + id - 3430).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3494 and id <= 3557: return (15051136 + id - 3494).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3558 and id <= 3621: return (15051392 + id - 3558).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3622 and id <= 3685: return (15051648 + id - 3622).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3686 and id <= 3749: return (15051904 + id - 3686).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3750 and id <= 3813: return (15052160 + id - 3750).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3814 and id <= 3877: return (15052416 + id - 3814).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3878 and id <= 3941: return (15052672 + id - 3878).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 3942 and id <= 4005: return (15052928 + id - 3942).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4006 and id <= 4069: return (15053184 + id - 4006).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4070 and id <= 4133: return (15053440 + id - 4070).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4134 and id <= 4197: return (15053696 + id - 4134).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4198 and id <= 4261: return (15053952 + id - 4198).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4262 and id <= 4325: return (15054208 + id - 4262).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4326 and id <= 4389: return (15054464 + id - 4326).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4390 and id <= 4453: return (15054720 + id - 4390).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4454 and id <= 4517: return (15054976 + id - 4454).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4518 and id <= 4581: return (15055232 + id - 4518).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4582 and id <= 4645: return (15055488 + id - 4582).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4646 and id <= 4709: return (15055744 + id - 4646).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4710 and id <= 4773: return (15056000 + id - 4710).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4774 and id <= 4837: return (15056256 + id - 4774).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4838 and id <= 4901: return (15056512 + id - 4838).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4902 and id <= 4965: return (15056768 + id - 4902).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 4966 and id <= 5029: return (15106176 + id - 4966).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5030 and id <= 5093: return (15106432 + id - 5030).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5094 and id <= 5157: return (15106688 + id - 5094).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5158 and id <= 5221: return (15106944 + id - 5158).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5222 and id <= 5285: return (15107200 + id - 5222).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5286 and id <= 5349: return (15107456 + id - 5286).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5350 and id <= 5413: return (15107712 + id - 5350).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5414 and id <= 5477: return (15107968 + id - 5414).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5478 and id <= 5541: return (15108224 + id - 5478).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5542 and id <= 5605: return (15108480 + id - 5542).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5606 and id <= 5669: return (15108736 + id - 5606).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5670 and id <= 5733: return (15108992 + id - 5670).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5734 and id <= 5797: return (15109248 + id - 5734).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5798 and id <= 5861: return (15109504 + id - 5798).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5862 and id <= 5925: return (15109760 + id - 5862).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5926 and id <= 5989: return (15110016 + id - 5926).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 5990 and id <= 6053: return (15110272 + id - 5990).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6054 and id <= 6117: return (15110528 + id - 6054).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6118 and id <= 6181: return (15110784 + id - 6118).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6182 and id <= 6245: return (15111040 + id - 6182).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6246 and id <= 6309: return (15111296 + id - 6246).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6310 and id <= 6373: return (15111552 + id - 6310).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6374 and id <= 6437: return (15111808 + id - 6374).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6438 and id <= 6501: return (15112064 + id - 6438).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6502 and id <= 6565: return (15112320 + id - 6502).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6566 and id <= 6629: return (15112576 + id - 6566).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6630 and id <= 6693: return (15112832 + id - 6630).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6694 and id <= 6757: return (15113088 + id - 6694).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6758 and id <= 6821: return (15113344 + id - 6758).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6822 and id <= 6885: return (15113600 + id - 6822).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6886 and id <= 6949: return (15113856 + id - 6886).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 6950 and id <= 7013: return (15114112 + id - 6950).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7014 and id <= 7077: return (15114368 + id - 7014).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7078 and id <= 7141: return (15114624 + id - 7078).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7142 and id <= 7205: return (15114880 + id - 7142).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7206 and id <= 7269: return (15115136 + id - 7206).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7270 and id <= 7333: return (15115392 + id - 7270).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7334 and id <= 7397: return (15115648 + id - 7334).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7398 and id <= 7461: return (15115904 + id - 7398).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7462 and id <= 7525: return (15116160 + id - 7462).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7526 and id <= 7589: return (15116416 + id - 7526).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7590 and id <= 7653: return (15116672 + id - 7590).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7654 and id <= 7717: return (15116928 + id - 7654).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7718 and id <= 7781: return (15117184 + id - 7718).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7782 and id <= 7845: return (15117440 + id - 7782).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7846 and id <= 7909: return (15117696 + id - 7846).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7910 and id <= 7973: return (15117952 + id - 7910).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 7974 and id <= 8037: return (15118208 + id - 7974).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8038 and id <= 8101: return (15118464 + id - 8038).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8102 and id <= 8165: return (15118720 + id - 8102).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8166 and id <= 8229: return (15118976 + id - 8166).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8230 and id <= 8293: return (15119232 + id - 8230).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8294 and id <= 8357: return (15119488 + id - 8294).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8358 and id <= 8421: return (15119744 + id - 8358).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8422 and id <= 8485: return (15120000 + id - 8422).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8486 and id <= 8549: return (15120256 + id - 8486).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8550 and id <= 8613: return (15120512 + id - 8550).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8614 and id <= 8677: return (15120768 + id - 8614).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8678 and id <= 8741: return (15121024 + id - 8678).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8742 and id <= 8805: return (15121280 + id - 8742).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8806 and id <= 8869: return (15121536 + id - 8806).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8870 and id <= 8933: return (15121792 + id - 8870).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8934 and id <= 8997: return (15122048 + id - 8934).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 8998 and id <= 9061: return (15122304 + id - 8998).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9062 and id <= 9125: return (15171712 + id - 9062).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9126 and id <= 9189: return (15171968 + id - 9126).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9190 and id <= 9253: return (15172224 + id - 9190).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9254 and id <= 9317: return (15172480 + id - 9254).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9318 and id <= 9381: return (15172736 + id - 9318).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9382 and id <= 9445: return (15172992 + id - 9382).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9446 and id <= 9509: return (15173248 + id - 9446).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9510 and id <= 9573: return (15173504 + id - 9510).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9574 and id <= 9637: return (15173760 + id - 9574).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9638 and id <= 9701: return (15174016 + id - 9638).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9702 and id <= 9765: return (15174272 + id - 9702).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9766 and id <= 9829: return (15174528 + id - 9766).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9830 and id <= 9893: return (15174784 + id - 9830).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9894 and id <= 9957: return (15175040 + id - 9894).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 9958 and id <= 10021: return (15175296 + id - 9958).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10022 and id <= 10085: return (15175552 + id - 10022).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10086 and id <= 10149: return (15175808 + id - 10086).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10150 and id <= 10213: return (15176064 + id - 10150).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10214 and id <= 10277: return (15176320 + id - 10214).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10278 and id <= 10341: return (15176576 + id - 10278).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10342 and id <= 10405: return (15176832 + id - 10342).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10406 and id <= 10469: return (15177088 + id - 10406).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10470 and id <= 10533: return (15177344 + id - 10470).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10534 and id <= 10597: return (15177600 + id - 10534).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10598 and id <= 10661: return (15177856 + id - 10598).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10662 and id <= 10725: return (15178112 + id - 10662).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10726 and id <= 10789: return (15178368 + id - 10726).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10790 and id <= 10853: return (15178624 + id - 10790).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10854 and id <= 10917: return (15178880 + id - 10854).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10918 and id <= 10981: return (15179136 + id - 10918).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 10982 and id <= 11045: return (15179392 + id - 10982).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11046 and id <= 11109: return (15179648 + id - 11046).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11110 and id <= 11173: return (15179904 + id - 11110).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11174 and id <= 11237: return (15180160 + id - 11174).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11238 and id <= 11301: return (15180416 + id - 11238).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11302 and id <= 11365: return (15180672 + id - 11302).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11366 and id <= 11429: return (15180928 + id - 11366).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11430 and id <= 11493: return (15181184 + id - 11430).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11494 and id <= 11557: return (15181440 + id - 11494).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11558 and id <= 11621: return (15181696 + id - 11558).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11622 and id <= 11685: return (15181952 + id - 11622).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11686 and id <= 11749: return (15182208 + id - 11686).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11750 and id <= 11813: return (15182464 + id - 11750).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11814 and id <= 11877: return (15182720 + id - 11814).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11878 and id <= 11941: return (15182976 + id - 11878).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 11942 and id <= 12005: return (15183232 + id - 11942).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12006 and id <= 12069: return (15183488 + id - 12006).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12070 and id <= 12133: return (15183744 + id - 12070).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12134 and id <= 12197: return (15184000 + id - 12134).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12198 and id <= 12261: return (15184256 + id - 12198).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12262 and id <= 12325: return (15184512 + id - 12262).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12326 and id <= 12389: return (15184768 + id - 12326).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12390 and id <= 12453: return (15185024 + id - 12390).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12454 and id <= 12517: return (15185280 + id - 12454).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12518 and id <= 12581: return (15185536 + id - 12518).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12582 and id <= 12645: return (15185792 + id - 12582).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12646 and id <= 12709: return (15186048 + id - 12646).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12710 and id <= 12773: return (15186304 + id - 12710).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12774 and id <= 12837: return (15186560 + id - 12774).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12838 and id <= 12901: return (15186816 + id - 12838).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12902 and id <= 12965: return (15187072 + id - 12902).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 12966 and id <= 13029: return (15187328 + id - 12966).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13030 and id <= 13093: return (15187584 + id - 13030).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13094 and id <= 13157: return (15187840 + id - 13094).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13158 and id <= 13221: return (15237248 + id - 13158).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13222 and id <= 13285: return (15237504 + id - 13222).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13286 and id <= 13349: return (15237760 + id - 13286).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13350 and id <= 13413: return (15238016 + id - 13350).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13414 and id <= 13477: return (15238272 + id - 13414).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13478 and id <= 13541: return (15238528 + id - 13478).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13542 and id <= 13605: return (15238784 + id - 13542).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13606 and id <= 13669: return (15239040 + id - 13606).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13670 and id <= 13733: return (15239296 + id - 13670).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13734 and id <= 13797: return (15239552 + id - 13734).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13798 and id <= 13861: return (15239808 + id - 13798).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13862 and id <= 13925: return (15240064 + id - 13862).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13926 and id <= 13989: return (15240320 + id - 13926).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 13990 and id <= 14053: return (15240576 + id - 13990).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14054 and id <= 14117: return (15240832 + id - 14054).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14118 and id <= 14181: return (15241088 + id - 14118).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14182 and id <= 14245: return (15241344 + id - 14182).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14246 and id <= 14309: return (15241600 + id - 14246).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14310 and id <= 14373: return (15241856 + id - 14310).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14374 and id <= 14437: return (15242112 + id - 14374).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14438 and id <= 14501: return (15242368 + id - 14438).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14502 and id <= 14565: return (15242624 + id - 14502).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14566 and id <= 14629: return (15242880 + id - 14566).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14630 and id <= 14693: return (15243136 + id - 14630).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14694 and id <= 14757: return (15243392 + id - 14694).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14758 and id <= 14821: return (15243648 + id - 14758).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14822 and id <= 14885: return (15243904 + id - 14822).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14886 and id <= 14949: return (15244160 + id - 14886).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 14950 and id <= 15013: return (15244416 + id - 14950).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15014 and id <= 15077: return (15244672 + id - 15014).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15078 and id <= 15141: return (15244928 + id - 15078).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15142 and id <= 15205: return (15245184 + id - 15142).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15206 and id <= 15269: return (15245440 + id - 15206).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15270 and id <= 15333: return (15245696 + id - 15270).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15334 and id <= 15397: return (15245952 + id - 15334).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15398 and id <= 15461: return (15246208 + id - 15398).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15462 and id <= 15525: return (15246464 + id - 15462).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15526 and id <= 15589: return (15246720 + id - 15526).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15590 and id <= 15653: return (15246976 + id - 15590).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15654 and id <= 15717: return (15247232 + id - 15654).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15718 and id <= 15781: return (15247488 + id - 15718).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15782 and id <= 15845: return (15247744 + id - 15782).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15846 and id <= 15909: return (15248000 + id - 15846).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15910 and id <= 15973: return (15248256 + id - 15910).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 15974 and id <= 16037: return (15248512 + id - 15974).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16038 and id <= 16101: return (15248768 + id - 16038).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16102 and id <= 16165: return (15249024 + id - 16102).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16166 and id <= 16229: return (15249280 + id - 16166).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16230 and id <= 16293: return (15249536 + id - 16230).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16294 and id <= 16357: return (15249792 + id - 16294).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16358 and id <= 16421: return (15250048 + id - 16358).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16422 and id <= 16485: return (15250304 + id - 16422).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16486 and id <= 16549: return (15250560 + id - 16486).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16550 and id <= 16613: return (15250816 + id - 16550).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16614 and id <= 16677: return (15251072 + id - 16614).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16678 and id <= 16741: return (15251328 + id - 16678).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16742 and id <= 16805: return (15251584 + id - 16742).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16806 and id <= 16869: return (15251840 + id - 16806).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16870 and id <= 16933: return (15252096 + id - 16870).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16934 and id <= 16997: return (15252352 + id - 16934).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 16998 and id <= 17061: return (15252608 + id - 16998).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17062 and id <= 17125: return (15252864 + id - 17062).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17126 and id <= 17189: return (15253120 + id - 17126).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17190 and id <= 17253: return (15253376 + id - 17190).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17254 and id <= 17317: return (15302784 + id - 17254).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17318 and id <= 17381: return (15303040 + id - 17318).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17382 and id <= 17445: return (15303296 + id - 17382).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17446 and id <= 17509: return (15303552 + id - 17446).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17510 and id <= 17573: return (15303808 + id - 17510).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17574 and id <= 17637: return (15304064 + id - 17574).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17638 and id <= 17701: return (15304320 + id - 17638).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17702 and id <= 17765: return (15304576 + id - 17702).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17766 and id <= 17829: return (15304832 + id - 17766).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17830 and id <= 17893: return (15305088 + id - 17830).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17894 and id <= 17957: return (15305344 + id - 17894).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 17958 and id <= 18021: return (15305600 + id - 17958).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18022 and id <= 18085: return (15305856 + id - 18022).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18086 and id <= 18149: return (15306112 + id - 18086).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18150 and id <= 18213: return (15306368 + id - 18150).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18214 and id <= 18277: return (15306624 + id - 18214).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18278 and id <= 18341: return (15306880 + id - 18278).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18342 and id <= 18405: return (15307136 + id - 18342).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18406 and id <= 18469: return (15307392 + id - 18406).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18470 and id <= 18533: return (15307648 + id - 18470).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18534 and id <= 18597: return (15307904 + id - 18534).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18598 and id <= 18661: return (15308160 + id - 18598).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18662 and id <= 18725: return (15308416 + id - 18662).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18726 and id <= 18789: return (15308672 + id - 18726).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18790 and id <= 18853: return (15308928 + id - 18790).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18854 and id <= 18917: return (15309184 + id - 18854).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18918 and id <= 18981: return (15309440 + id - 18918).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 18982 and id <= 19045: return (15309696 + id - 18982).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19046 and id <= 19109: return (15309952 + id - 19046).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19110 and id <= 19173: return (15310208 + id - 19110).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19174 and id <= 19237: return (15310464 + id - 19174).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19238 and id <= 19301: return (15310720 + id - 19238).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19302 and id <= 19365: return (15310976 + id - 19302).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19366 and id <= 19429: return (15311232 + id - 19366).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19430 and id <= 19493: return (15311488 + id - 19430).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19494 and id <= 19557: return (15311744 + id - 19494).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19558 and id <= 19621: return (15312000 + id - 19558).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19622 and id <= 19685: return (15312256 + id - 19622).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19686 and id <= 19749: return (15312512 + id - 19686).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19750 and id <= 19813: return (15312768 + id - 19750).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19814 and id <= 19877: return (15313024 + id - 19814).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19878 and id <= 19941: return (15313280 + id - 19878).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 19942 and id <= 20005: return (15313536 + id - 19942).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20006 and id <= 20069: return (15313792 + id - 20006).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20070 and id <= 20133: return (15314048 + id - 20070).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20134 and id <= 20197: return (15314304 + id - 20134).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20198 and id <= 20261: return (15314560 + id - 20198).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20262 and id <= 20325: return (15314816 + id - 20262).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20326 and id <= 20389: return (15315072 + id - 20326).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20390 and id <= 20453: return (15315328 + id - 20390).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20454 and id <= 20517: return (15315584 + id - 20454).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20518 and id <= 20581: return (15315840 + id - 20518).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20582 and id <= 20645: return (15316096 + id - 20582).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20646 and id <= 20709: return (15316352 + id - 20646).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20710 and id <= 20773: return (15316608 + id - 20710).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20774 and id <= 20837: return (15316864 + id - 20774).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20838 and id <= 20901: return (15317120 + id - 20838).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20902 and id <= 20965: return (15317376 + id - 20902).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 20966 and id <= 21029: return (15317632 + id - 20966).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21030 and id <= 21093: return (15317888 + id - 21030).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21094 and id <= 21157: return (15318144 + id - 21094).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21158 and id <= 21221: return (15318400 + id - 21158).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21222 and id <= 21285: return (15318656 + id - 21222).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21286 and id <= 21349: return (15318912 + id - 21286).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21350 and id <= 21413: return (15711360 + id - 21350).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21414 and id <= 21477: return (15711616 + id - 21414).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21478 and id <= 21509: return (15711872 + id - 21478).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21510 and id <= 21573: return (14844032 + id - 21510).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21574 and id <= 21637: return (14844288 + id - 21574).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 21638: return (14849152).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21639 and id <= 21654: return (14850464 + id - 21639).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21655 and id <= 21670: return (14850176 + id - 21655).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21671 and id <= 21702: return (49824 + id - 21671).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21703 and id <= 21750: return (50048 + id - 21703).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21751 and id <= 21798: return (50304 + id - 21751).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21799 and id <= 21846: return (50560 + id - 21799).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21847 and id <= 21894: return (50816 + id - 21847).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21895 and id <= 21942: return (51072 + id - 21895).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21943 and id <= 21990: return (51328 + id - 21943).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 21991 and id <= 22038: return (51584 + id - 21991).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22039 and id <= 22086: return (51840 + id - 22039).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22087 and id <= 22134: return (52096 + id - 22087).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22135 and id <= 22182: return (52352 + id - 22135).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22183 and id <= 22230: return (52608 + id - 22183).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22231 and id <= 22294: return (52864 + id - 22231).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22295 and id <= 22358: return (53120 + id - 22295).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22359 and id <= 22422: return (53376 + id - 22359).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22423 and id <= 22486: return (53632 + id - 22423).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22487 and id <= 22550: return (53888 + id - 22487).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22551 and id <= 22614: return (54144 + id - 22551).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22615 and id <= 22678: return (54400 + id - 22615).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22679 and id <= 22742: return (54656 + id - 22679).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22743 and id <= 22806: return (54912 + id - 22743).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22807 and id <= 22870: return (55168 + id - 22807).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22871 and id <= 22934: return (55424 + id - 22871).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22935 and id <= 22998: return (55680 + id - 22935).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 22999 and id <= 23062: return (55936 + id - 22999).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23063 and id <= 23126: return (56192 + id - 23063).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23127 and id <= 23158: return (15710608 + id - 23127).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23159 and id <= 23222: return (14845312 + id - 23159).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23223 and id <= 23286: return (14845568 + id - 23223).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23287 and id <= 23350: return (14845824 + id - 23287).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23351 and id <= 23414: return (14846080 + id - 23351).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23415 and id <= 23478: return (14846336 + id - 23415).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23479 and id <= 23542: return (14846592 + id - 23479).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23543 and id <= 23606: return (14846848 + id - 23543).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23607 and id <= 23670: return (14847104 + id - 23607).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23671 and id <= 23734: return (14847360 + id - 23671).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23735 and id <= 23798: return (14847616 + id - 23735).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23799 and id <= 23862: return (14847872 + id - 23799).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23863 and id <= 23926: return (14848384 + id - 23863).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23927 and id <= 23990: return (14848640 + id - 23927).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 23991 and id <= 24054: return (14848896 + id - 23991).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 24055 and id <= 24118: return (14912640 + id - 24055).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 24119 and id <= 24182: return (14912896 + id - 24119).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 24183 and id <= 24246: return (14913152 + id - 24183).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 24247 and id <= 24310: return (14913408 + id - 24247).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 24311 and id <= 24374: return (14845056 + id - 24311).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 24375 and id <= 24406: return (14849696 + id - 24375).to_bytes(16, 'big').decode("utf-8")[-1]
	if id >= 24407 and id <= 24470: return (14849920 + id - 24407).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24471: return (14851229).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24472: return (14851228).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24473: return (14851492).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24474: return (15710350).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24475: return (15710351).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24476: return (14849153).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24477: return (15712163).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24478: return (14850963).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24479: return (14849160).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24480: return (14851263).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24481: return (14850432).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24482: return (14851745).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24483: return (14849157).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24484: return (14850434).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24485: return (14850730).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24486: return (14849155).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24487: return (15712165).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24488: return (14849164).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24489: return (14849168).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24490: return (14727569).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24491: return (14849672).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24492: return (14851221).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24493: return (50103).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24494: return (14849154).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24495: return (14849167).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24496: return (14851239).to_bytes(16, 'big').decode("utf-8")[-1]
	if id == 24497: return (14850195).to_bytes(16, 'big').decode("utf-8")[-1]
	raise Exception("unexpected id : "+id)
