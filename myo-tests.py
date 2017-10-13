import myo as libmyo
import time

libmyo.init()

class Listener(libmyo.DeviceListener):

        def on_connect(self, myo, timestamp):
            print("Hello, Myo!")

        def on_disconnect(self, myo, timestamp):
            print("Goodbye, Myo!")

        def on_orientation_data(self, myo, timestamp, quat):
            print("Orientation:", quat.x, quat.y, quat.z, quat.w)

        def on_pose(self, myo, timestamp, pose):
            if pose == libmyo.Pose.fist:
                print("Don't show me 'ya fist!")
                return False  # Stops the Hub


feed = libmyo.device_listener.Feed()
hub = libmyo.Hub()
hub.run(1000, feed)
try:
    myo = feed.wait_for_single_device(timeout=10.0)  # seconds
    if not myo:
        print("No Myo connected after 10 seconds.")
        sys.exit()

    while hub.running and myo.connected:
        pose = myo.pose
        if pose == libmyo.Pose.fist:
            print("Fist!")
        elif pose == libmyo.Pose.fingers_spread:
        	print("Spread!")
except KeyboardInterrupt:
    print("Quitting...")
finally:
    hub.shutdown()

