the given python script is for forground moving mask detemination that is numpy 2d array.


>the video is read by using cv2.videocapture and then is divided into frames.
each frame is then deposited into the list named col_images.
>primarly the first frmae is converted into gray fomat from bgr format.
>then it is compared along with the very next frame and the object that changes its pixcels is masked.
>in the next step the thresholding is invoked and processed.
>after thresholding, dialation process is done to make the determined object more predictable.
> after this each frame is alinged and deposited to cv2.imshow method

To exit the final imshow frame enter q.

I would love to ask for the final code that removes the foreground so i can use it for educational purpose and improvement as mentioned in the mail.