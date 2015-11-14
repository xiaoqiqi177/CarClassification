#include <cv.h>
#include <highgui.h>
//#include <stdio.h>

IplImage* src = 0; 
IplImage* dst = 0; 
char* kind;

void on_mouse( int event, int x, int y, int flags, void* ustc)
{
	static CvPoint pre_pt (-1,-1);
	static CvPoint cur_pt = (-1,-1);
	CvFont font;
	cvInitFont(&font, CV_FONT_HERSHEY_SIMPLEX, 0.5, 0.5, 0, 1, CV_AA);
	char temp[16];
	
	if( event == CV_EVENT_LBUTTONDOWN )
	{
		cvCopy(dst,src);
		sprintf(temp,"(%d,%d)",x,y);
		//
		printf("%s %d %d ", kind, x, y);

		pre_pt = cvPoint(x,y);
		cvPutText(src,temp, pre_pt, &font, cvScalar(0,0, 0, 255));
		cvCircle( src, pre_pt, 3,cvScalar(255,0,0,0) ,CV_FILLED, CV_AA, 0 );
		cvShowImage( "src", src );
		cvCopy(src,dst);
	}
	else if( event == CV_EVENT_MOUSEMOVE && !(flags & CV_EVENT_FLAG_LBUTTON))
	{
		cvCopy(dst,src);
		sprintf(temp,"(%d,%d)",x,y);
		//		
		//printf("%d %d\n", x, y);
		
		cur_pt = cvPoint(x,y);		
		cvPutText(src,temp, cur_pt, &font, cvScalar(0,0, 0, 255));
		cvShowImage( "src", src );
	}
	else if( event == CV_EVENT_MOUSEMOVE && (flags & CV_EVENT_FLAG_LBUTTON))
	{
		cvCopy(dst,src);
		sprintf(temp,"(%d,%d)",x,y);
		//
		//printf("%d %d\n", x, y);
		
		cur_pt = cvPoint(x,y);		
		cvPutText(src,temp, cur_pt, &font, cvScalar(0,0, 0, 255));
		cvRectangle(src, pre_pt, cur_pt, cvScalar(0,255,0,0), 1, 8, 0 );
		cvShowImage( "src", src );
	}
	else if( event == CV_EVENT_LBUTTONUP )
	{
		sprintf(temp,"(%d,%d)",x,y);
		//
		printf("%d %d\n", x, y);
		
		cur_pt = cvPoint(x,y);		
		cvPutText(src,temp, cur_pt, &font, cvScalar(0,0, 0, 255));
		cvCircle( src, cur_pt, 3,cvScalar(255,0,0,0) ,CV_FILLED, CV_AA, 0 );
		cvRectangle( src, pre_pt, cur_pt, cvScalar(0,255,0,0), 1, 8, 0 );
		cvShowImage( "src", src );
		cvCopy(src,dst);
	}
}

int main(int argc, char** argv)
{
	src = cvLoadImage(argv[1],1);
	kind = argv[2]; 
	dst=cvCloneImage(src);
	cvNamedWindow("src",1);
	cvSetMouseCallback( "src", on_mouse, 0 );

	
	cvShowImage("src",src);
	cvWaitKey(0);

	cvDestroyAllWindows();
	cvReleaseImage(&src);
	cvReleaseImage(&dst);

	return 0;

}
