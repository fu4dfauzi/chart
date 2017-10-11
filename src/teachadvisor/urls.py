"""teachadvisor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from home.views import HomeView, PromotionView, ContactView, TermsAndConditionView, DisclaimerView, PrivacyPolicyView, RefundPolicyView, FAQView, CSupportView, TutorialsView, CareersView, PressView, PartnershipsView, Test
from home.charts import TeacherChart #StudentChart,

from teacher.views import TeacherCreate, TeacherUpdate, TeacherList, TeacherDetail, FavTeacherList
from opening.views import OpeningCreate, OpeningList, OpeningUpdate, OpeningDetail, FavOpeningList, POpeningList, POpeningListInactive
from student.views import StudentCreate, StudentUpdate, StudentList, StudentDetail
# from messaging.views import PostMessageView, MessageDetailView, OpeningSelectMsg, Oselectmsgc, Oselectmsgw, BlockSub
# from messaging.views import MessageListViewAll, MessageListViewMsg, MessageListViewPpl, MessageListViewWip, MessageListViewDon
from tags.views import FavTeacherSub, FavOpeningSub
# from orders.views import Accept, AcceptConf, OrderDetail, OrderDetailView, Withdraw, WithConf, OpeningConfirmAppOff, AppOffConf#, OpeningConfirmRej, RejectMsg
# from orderreview.views import OrderCancelReview, OrderCompleteReview, Finish, RecordMsg, ReviewListView, ReviewDetailView, ReviewList, OrderCompleteConfirm, ReviewDetail
# from billing.views import ImageSub, AddCredits, CheckOut, CheckOutFinal, Invoice, ImageSub, FeatureSub, AnalyticsSub, StudentBISub
# from notifications.views import allin, read, get_notifications_ajax, MsgCountView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^accounts/',include('allauth.urls')),
    url(r'^$', HomeView.as_view(), name='Home'),

    url(r'^contact/$', ContactView.as_view(), name='Contact'),
    # url(r'^promotions/$', PromotionView.as_view(), name='Promotions'),

    url(r'^termsandconditions/$', TermsAndConditionView.as_view(), name='TermsAndCondition'),
    url(r'^disclaimer/$', DisclaimerView.as_view(), name='Disclaimer'),
    url(r'^privacypolicy/$', PrivacyPolicyView.as_view(), name='PrivacyPolicy'),
    url(r'^refundpolicy/$', RefundPolicyView.as_view(), name='RefundPolicy'),

    url(r'^FAQ/$', FAQView.as_view(), name='FAQ'),
    url(r'^customersupport/$', CSupportView.as_view(), name='Customer_Support'),
    url(r'^tutorials/$', TutorialsView.as_view(), name='Tutorials'),

    url(r'^careers/$', CareersView.as_view(), name='Careers'),
    url(r'^press/$', PressView.as_view(), name='Press'),
    url(r'^partnership/$', PartnershipsView.as_view(), name='Partnership'),



    # url(r'^test/$', Test, name='Test'),

    # #billing and subscription
    # url(r'^billing/imagesub/$', ImageSub.as_view(), name='ImageSub'),
    # url(r'^billing/analyticssub/$', AnalyticsSub.as_view(), name='AnalyticsSub'),
    # url(r'^billing/studentbisub/$', StudentBISub.as_view(), name='StudentBISub'),
    # url(r'^billing/featuresub/$', FeatureSub.as_view(), name='FeatureSub'),
    # url(r'^billing/creditadd/$', AddCredits.as_view(), name='AddCredits'),
    # url(r'^billing/checkout/$', CheckOut.as_view(), name='CheckOut'),
    # url(r'^billing/checkout/final$', CheckOutFinal.as_view(), name='CheckOutFinal'),
    # url(r'^billing/checkout/invoice$', Invoice.as_view(), name='Invoice'),
    # url(r'^billing/subscription/$', ImageSub.as_view(), name='ImageSub'),

    #worker details
    url(r'^teacher/add/$', TeacherCreate.as_view(), name='TeacherCreate'),
    url(r'^teacher/$', TeacherList.as_view(), name='TeacherList'),
    url(r'^teacher/(?P<pk>[0-9]+)/edit$', TeacherUpdate.as_view(), name='TeacherUpdate'),
    url(r'^teacher/(?P<pk>[0-9]+)/$', TeacherDetail.as_view(), name='TeacherDetail'),

    #company details
    url(r'^student/add/$', StudentCreate.as_view(), name='StudentCreate'),
    url(r'^student/$', StudentList.as_view(), name='StudentList'), #to block when live
    url(r'^student/(?P<pk>[0-9]+)/edit$', StudentUpdate.as_view(), name='StudentUpdate'),
    url(r'^student/(?P<pk>[0-9]+)/$', StudentDetail.as_view(), name='StudentDetail'),

    #openings
    url(r'^opening/add/$', OpeningCreate.as_view(), name='OpeningCreate'),
    url(r'^opening/$', OpeningList.as_view(), name='OpeningList'),
    url(r'^opening/(?P<pk>[0-9]+)/edit$', OpeningUpdate.as_view(), name='OpeningUpdate'),
    url(r'^opening/(?P<pk>[0-9]+)/$', OpeningDetail.as_view(), name='OpeningDetail'),
    
    #openings that are specific to a company
    url(r'^popenings/$', POpeningList.as_view(), name='POpeningList'),
    url(r'^popeningsinact/$', POpeningListInactive.as_view(), name='POpeningListInactive'),

    # #messaging
    # url(r'^messaging/$', PostMessageView.as_view(), name='Messaging'),
    # url(r'^messagelistall/$', MessageListViewAll.as_view(), name='MessageListViewAll'),
    # url(r'^messagelistmsg/$', MessageListViewMsg.as_view(), name='MessageListViewMsg'),
    # url(r'^messagelistppl/$', MessageListViewPpl.as_view(), name='MessageListViewPpl'),
    # url(r'^messagelistwip/$', MessageListViewWip.as_view(), name='MessageListViewWip'),
    # url(r'^messagelistdon/$', MessageListViewDon.as_view(), name='MessageListViewDon'),


    # url(r'^messagedetail/(?P<pk>[0-9]+)/$', MessageDetailView.as_view(), name='MessageDetail'),

    # #favoriting openings or teacher
    # url(r'^teacher/(?P<pk>[0-9]+)/FavTeacherSub$', FavTeacherSub),
    # url(r'^opening/(?P<pk>[0-9]+)/FavOpeningSub$', FavOpeningSub),

    # #favorite lists
    # url(r'^teacher/favteacherlist$', FavTeacherList.as_view(), name='FavTeacherList'),
    # url(r'^opening/favopeninglist$', FavOpeningList.as_view(), name='FavOpeningList'),

    # #selecting opening to message for student
    # url(r'^openingselectmsg/$', OpeningSelectMsg.as_view(), name='OpeningSelectMsg'),
    # url(r'^openingselectmsg/Oselectmsgc$', Oselectmsgc, name='Oselectmsgc'),

    # #selecting opening to message for teacher
    # url(r'^opening/(?P<pk>[0-9]+)/Oselectmsgw$',Oselectmsgw),
    # url(r'^messagedetail/(?P<pk>[0-9]+)/appoffconf$', AppOffConf, name='AppOffConf'),
    # url(r'^opening/appoffconfirm$', OpeningConfirmAppOff.as_view(), name='OpeningConfirmAppOff'),

    # #get acceptance
    # url(r'^messagedetail/(?P<pk>[0-9]+)/accconf$', AcceptConf, name='AcceptConf'),
    # url(r'^messagedetail/Accept$',Accept.as_view(), name='Accept'),

    # #withdraw proposal
    # url(r'^messagedetail/(?P<pk>[0-9]+)/withconf$', WithConf, name='WithConf'),
    # url(r'^opening/withdraw$', Withdraw.as_view(), name='Withdraw'),
    
    # #block and unblock users
    # url(r'^messagedetail/(?P<pk>[0-9]+)/blocksub$', BlockSub, name='BlockSub'),


    # #viewing orders
    # # url(r'^order/$', OrderListView.as_view(), name='OrderList'),
    # url(r'^order/detail/$', OrderDetail, name='OrderDetail'),
    # url(r'^order/detail/view$', OrderDetailView.as_view(), name='OrderDetailView'),

    # #finish orders
    # url(r'^order/finish$', Finish, name='Finish'),
    # url(r'^order/completeconfirm$', OrderCompleteConfirm.as_view(), name='OrderCompleteConfirm'),

    # #completed or cancelled and ready for review    
    # url(r'^review/recordmsg$', RecordMsg, name='RecordMsg'),
    # url(r'^review/cancelreview/$', OrderCancelReview.as_view(), name='OrderCancelReview'),
    # url(r'^review/completereview/$', OrderCompleteReview.as_view(), name='OrderCompleteReview'),

    # #viewing reviews
    # url(r'^review/reviewlist$', ReviewList, name='ReviewList'),
    # url(r'^review/reviewlist/view$', ReviewListView.as_view(), name='ReviewListView'),
    
    # url(r'^review/reviewdetail/$', ReviewDetail, name='ReviewDetail'),
    # url(r'^review/reviewdetail/view$', ReviewDetailView.as_view(), name='ReviewDetailView'),

    # #notifications
    # url(r'^notifications/$', allin, name='notifications_all'),
    # url(r'^notifications/ajax/$', get_notifications_ajax, name='get_notifications_ajax'),
    # url(r'^notifications/(?P<id>\d+)/$', read, name='notifications_read'),
    # url(r'^notifications/count/$', MsgCountView.as_view(), name='msg_count'),

    # url(r'^examplepiechart/$', ExamplePieChart.as_view(), name='ExamplePieChart'),
    url(r'^teacherchart/$', TeacherChart.as_view(), name='TeacherChart'),
    # url(r'^studentchart/$', StudentChart.as_view(), name='StudentChart'),


]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
