from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import CanConcatenateVideos  # Import the permission class
from moviepy import VideoFileClip, concatenate_videoclips

class ConcatenateVideosAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Fetch video files from request
        video1 = request.FILES.get("video1")
        video2 = request.FILES.get("video2")

        if not video1 or not video2:
            return Response({"error": "Please provide two video files."}, status=400)

        clip1 = VideoFileClip(video1)
        clip2 = VideoFileClip(video2)
        final_clip = concatenate_videoclips([clip1, clip2])

        # Save final video
        final_clip.write_videofile("final_video.mp4", codec="libx264", fps=24)
        
        return Response({"message": "Videos successfully concatenated."}, status=200)



