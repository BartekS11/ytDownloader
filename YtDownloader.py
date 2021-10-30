import logging
import os
from pytube import YouTube
import argparse


class YtDownloader(object):
    def __init__(self, url_link, playlist_link=None, res='1080p'):
        self.url_link = url_link
        self.res = res
        self.playlist_link = playlist_link
        self.check_file_exists()
        self.download_yt_file()
        self.choose = True

    def yes_no_func(self):
        yes = {'yes', 'y', 'ye', ' '}
        no = {'no', 'n'}
        print('Please respond [Y/N] ')
        print('-' * 50)
        choice = input().lower()
        if str(choice) in yes:
            self.choose = True
            return self.choose
        elif str(choice) in no:
            self.choose = False
            return self.choose
        else:
            print('Respond with correct words (yes or no)')
            self.yes_no_func()

    def del_file(self, os_path):
        os.remove(os_path)
        print(f"File has been deleted {os_path} ")

    def get_yt_link_and_validate_it(self, url_link):
        valid_url_link = url_link
        print('Link validated correctly')
        return valid_url_link

    def get_video_title(self):
        yt_link = YouTube(self.url_link)
        print(yt_link.title)
        return yt_link.title

    def download_yt_file(self):
        yt_link = self.get_yt_link_and_validate_it(self.url_link)
        yt = YouTube(yt_link)
        yt = yt.streams.filter(file_extension='mp4', res=self.res).first()
        yt.download('/home/stvhh/PycharmProjects/ytDownloader')

    def check_file_exists(self):
        dir_path = '/home/stvhh/PycharmProjects/ytDownloader'
        yt_title = self.get_video_title()
        full_title = dir_path + '/' + str(yt_title) + '.mp4'
        print(f'Checking file location...{full_title}')
        print(50 * '-')
        if os.path.isfile(full_title):
            print('File already exists!!! Would you like to delete it?')
            if self.yes_no_func():
                self.del_file(full_title)
            else:
                print('File is downloading | ' * 3)


if __name__ == '__main__':
    logging.info("Use -r flag for res, default is 1080p, use -v flag to enter yt url")
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--video', help='Download single video')
    parser.add_argument('-l', '--link', help='Yt video url link')
    parser.add_argument('-r', '--res', help='Choose resolution, preferred 1920x1080')
    args = parser.parse_args()

    print(50 * '-')
    if args.video and args.res:
        ytDownloader = YtDownloader(args.video, args.res)
    elif args.video:
        ytDownloader = YtDownloader(args.video)
    else:
        logging.error('Zly link/brak linku do filmu Youtube')
