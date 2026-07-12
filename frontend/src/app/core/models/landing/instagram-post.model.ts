export interface InstagramChild {
  media_url: string;
  media_type?: 'IMAGE' | 'VIDEO';
  thumbnail_url?: string;
}

export interface InstagramPost {
  id: string;
  caption: string | null;
  media_type: 'IMAGE' | 'VIDEO' | 'CAROUSEL_ALBUM';
  media_url: string;
  permalink: string;
  thumbnail_url?: string;
  timestamp: string;
  children?: {
    data: InstagramChild[];
  };
}
