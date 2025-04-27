card1(X).
card2(X).

+!g1_x_p1win_:
	card1(a) &
	card2(a)
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card1(a) &
	card2(q)
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	card1(a) &
	card2(k)
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card1(q) &
	card2(a)
	<-
	.drop_all_intentions;
	keep;
	true.

+!g1_x_p1win_:
	card1(q) &
	card2(q)
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card1(q) &
	card2(k)
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card1(k) &
	card2(a)
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card1(k) &
	card2(q)
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card1(k) &
	card2(k)
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card1(a) &
	poss(card2(a)) &
	poss(card2(q)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	card1(a) &
	poss(card2(a)) &
	poss(card2(q))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	card1(a) &
	poss(card2(a)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card1(a) &
	poss(card2(q)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	card1(q) &
	poss(card2(a)) &
	poss(card2(q)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	keep;
	true.

+!g1_x_p1win_:
	card1(q) &
	poss(card2(a)) &
	poss(card2(q))
	<-
	.drop_all_intentions;
	keep;
	true.

+!g1_x_p1win_:
	card1(q) &
	poss(card2(a)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	keep;
	true.

+!g1_x_p1win_:
	card1(q) &
	poss(card2(q)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card1(k) &
	poss(card2(a)) &
	poss(card2(q)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card1(k) &
	poss(card2(a)) &
	poss(card2(q))
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card1(k) &
	poss(card2(a)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card1(k) &
	poss(card2(q)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card2(a) &
	poss(card1(a)) &
	poss(card1(q)) &
	poss(card1(k))
	<-
	.drop_all_intentions;
	keep;
	true.

+!g1_x_p1win_:
	card2(a) &
	poss(card1(a)) &
	poss(card1(q))
	<-
	.drop_all_intentions;
	keep;
	true.

+!g1_x_p1win_:
	card2(a) &
	poss(card1(a)) &
	poss(card1(k))
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card2(a) &
	poss(card1(q)) &
	poss(card1(k))
	<-
	.drop_all_intentions;
	keep;
	true.

+!g1_x_p1win_:
	card2(q) &
	poss(card1(a)) &
	poss(card1(q)) &
	poss(card1(k))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	card2(q) &
	poss(card1(a)) &
	poss(card1(q))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	card2(q) &
	poss(card1(a)) &
	poss(card1(k))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	card2(q) &
	poss(card1(q)) &
	poss(card1(k))
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card2(k) &
	poss(card1(a)) &
	poss(card1(q)) &
	poss(card1(k))
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card2(k) &
	poss(card1(a)) &
	poss(card1(q))
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card2(k) &
	poss(card1(a)) &
	poss(card1(k))
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	card2(k) &
	poss(card1(q)) &
	poss(card1(k))
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	poss(card1(a)) &
	poss(card1(q)) &
	poss(card1(k)) &
	poss(card2(a)) &
	poss(card2(q)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	poss(card1(a)) &
	poss(card1(q)) &
	poss(card1(k)) &
	poss(card2(a)) &
	poss(card2(q))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	poss(card1(a)) &
	poss(card1(q)) &
	poss(card1(k)) &
	poss(card2(a)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	keep;
	true.

+!g1_x_p1win_:
	poss(card1(a)) &
	poss(card1(q)) &
	poss(card1(k)) &
	poss(card2(q)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	poss(card1(a)) &
	poss(card1(q)) &
	poss(card2(a)) &
	poss(card2(q)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	poss(card1(a)) &
	poss(card1(q)) &
	poss(card2(a)) &
	poss(card2(q))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	poss(card1(a)) &
	poss(card1(q)) &
	poss(card2(a)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	keep;
	true.

+!g1_x_p1win_:
	poss(card1(a)) &
	poss(card1(q)) &
	poss(card2(q)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	poss(card1(a)) &
	poss(card1(k)) &
	poss(card2(a)) &
	poss(card2(q)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	poss(card1(a)) &
	poss(card1(k)) &
	poss(card2(a)) &
	poss(card2(q))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	poss(card1(a)) &
	poss(card1(k)) &
	poss(card2(a)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	true.

+!g1_x_p1win_:
	poss(card1(a)) &
	poss(card1(k)) &
	poss(card2(q)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	swap;
	true.

+!g1_x_p1win_:
	poss(card1(q)) &
	poss(card1(k)) &
	poss(card2(a)) &
	poss(card2(q)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	keep;
	true.

+!g1_x_p1win_:
	poss(card1(q)) &
	poss(card1(k)) &
	poss(card2(a)) &
	poss(card2(q))
	<-
	.drop_all_intentions;
	keep;
	true.

+!g1_x_p1win_:
	poss(card1(q)) &
	poss(card1(k)) &
	poss(card2(a)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	keep;
	true.

+!g1_x_p1win_:
	poss(card1(q)) &
	poss(card1(k)) &
	poss(card2(q)) &
	poss(card2(k))
	<-
	.drop_all_intentions;
	true.

