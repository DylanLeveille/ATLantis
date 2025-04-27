columnba(X).
columnra(X).
rowba(X).
rowra(X).
treasuremined(X).

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(0) &
	rowba(0) &
	rowra(0)
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(0) &
	rowba(0) &
	rowra(1)
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(0) &
	rowba(1) &
	rowra(0)
	<-
	.drop_all_intentions;
	right;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(0) &
	rowba(1) &
	rowra(1)
	<-
	.drop_all_intentions;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(1) &
	rowba(0) &
	rowra(0)
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(1) &
	rowba(0) &
	rowra(1)
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(1) &
	rowba(1) &
	rowra(0)
	<-
	.drop_all_intentions;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(1) &
	rowba(1) &
	rowra(1)
	<-
	.drop_all_intentions;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(0) &
	rowba(0) &
	rowra(0)
	<-
	.drop_all_intentions;
	down;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(0) &
	rowba(0) &
	rowra(1)
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(0) &
	rowba(1) &
	rowra(0)
	<-
	.drop_all_intentions;
	mine;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(0) &
	rowba(1) &
	rowra(1)
	<-
	.drop_all_intentions;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(1) &
	rowba(0) &
	rowra(0)
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(1) &
	rowba(0) &
	rowra(1)
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(1) &
	rowba(1) &
	rowra(0)
	<-
	.drop_all_intentions;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(1) &
	rowba(1) &
	rowra(1)
	<-
	.drop_all_intentions;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(0) &
	rowba(0) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(0) &
	rowba(1) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	right;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(1) &
	rowba(0) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(1) &
	rowba(1) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(0) &
	rowba(0) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(0) &
	rowba(1) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	mine;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(1) &
	rowba(0) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(1) &
	rowba(1) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(0) &
	rowra(0) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(0) &
	rowra(1) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(1) &
	rowra(0) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(1) &
	rowra(1) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(0) &
	rowra(0) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(0) &
	rowra(1) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(1) &
	rowra(0) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(1) &
	rowra(1) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	rowba(0) &
	rowra(0) &
	poss(columnra(0)) &
	poss(columnra(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	rowba(0) &
	rowra(1) &
	poss(columnra(0)) &
	poss(columnra(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	rowba(1) &
	rowra(0) &
	poss(columnra(0)) &
	poss(columnra(1))
	<-
	.drop_all_intentions;
	right;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	rowba(1) &
	rowra(1) &
	poss(columnra(0)) &
	poss(columnra(1))
	<-
	.drop_all_intentions;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	rowba(0) &
	rowra(0) &
	poss(columnra(0)) &
	poss(columnra(1))
	<-
	.drop_all_intentions;
	down;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	rowba(0) &
	rowra(1) &
	poss(columnra(0)) &
	poss(columnra(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	rowba(1) &
	rowra(0) &
	poss(columnra(0)) &
	poss(columnra(1))
	<-
	.drop_all_intentions;
	mine;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	rowba(1) &
	rowra(1) &
	poss(columnra(0)) &
	poss(columnra(1))
	<-
	.drop_all_intentions;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(0) &
	rowba(0) &
	rowra(0) &
	poss(columnba(0)) &
	poss(columnba(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(0) &
	rowba(0) &
	rowra(1) &
	poss(columnba(0)) &
	poss(columnba(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(0) &
	rowba(1) &
	rowra(0) &
	poss(columnba(0)) &
	poss(columnba(1))
	<-
	.drop_all_intentions;
	right;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(0) &
	rowba(1) &
	rowra(1) &
	poss(columnba(0)) &
	poss(columnba(1))
	<-
	.drop_all_intentions;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(1) &
	rowba(0) &
	rowra(0) &
	poss(columnba(0)) &
	poss(columnba(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(1) &
	rowba(0) &
	rowra(1) &
	poss(columnba(0)) &
	poss(columnba(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(1) &
	rowba(1) &
	rowra(0) &
	poss(columnba(0)) &
	poss(columnba(1))
	<-
	.drop_all_intentions;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(1) &
	rowba(1) &
	rowra(1) &
	poss(columnba(0)) &
	poss(columnba(1))
	<-
	.drop_all_intentions;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(0) &
	poss(rowba(0)) &
	poss(rowba(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	columnra(1) &
	poss(rowba(0)) &
	poss(rowba(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(0) &
	poss(rowba(0)) &
	poss(rowba(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	columnra(1) &
	poss(rowba(0)) &
	poss(rowba(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	rowba(0) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	rowba(1) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	rowba(0) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	rowba(1) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	rowra(0) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	rowra(1) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	rowra(0) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	rowra(1) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(0) &
	rowba(0) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(0) &
	rowba(1) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(1) &
	rowba(0) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(1) &
	rowba(1) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(0) &
	rowra(0) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	mine;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(0) &
	rowra(1) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(1) &
	rowra(0) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(1) &
	rowra(1) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	rowba(0) &
	rowra(0) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(columnra(0)) &
	poss(columnra(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	rowba(0) &
	rowra(1) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(columnra(0)) &
	poss(columnra(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	rowba(1) &
	rowra(0) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(columnra(0)) &
	poss(columnra(1))
	<-
	.drop_all_intentions;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	rowba(1) &
	rowra(1) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(columnra(0)) &
	poss(columnra(1))
	<-
	.drop_all_intentions;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(0) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowba(0)) &
	poss(rowba(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnba(1) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowba(0)) &
	poss(rowba(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(0) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(rowba(0)) &
	poss(rowba(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	columnra(1) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(rowba(0)) &
	poss(rowba(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	rowba(0) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	rowba(1) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	rowra(0) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	right;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	rowra(1) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowba(0)) &
	poss(rowba(1))
	<-
	.drop_all_intentions;
	down;
	true.

+!g1___f_batreasure_and_ratreasure__:
	treasuremined(false) &
	poss(columnba(0)) &
	poss(columnba(1)) &
	poss(columnra(0)) &
	poss(columnra(1)) &
	poss(rowba(0)) &
	poss(rowba(1)) &
	poss(rowra(0)) &
	poss(rowra(1))
	<-
	.drop_all_intentions;
	down;
	true.

