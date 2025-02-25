import * as React from 'react';
import Card from '@mui/material/Card';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';

import { News } from './News'; // Ensure this News type is updated to match your new API structure

interface NewsCardProps {
  newsItem: News;
  language: 'ar' | 'en';
}

export default function NewsCard({ newsItem, language }: NewsCardProps) {
  const [expanded, setExpanded] = React.useState(false);
  const [showAllSources, setShowAllSources] = React.useState(false);
  const isRTL = language === 'ar';

  const visibleSources = showAllSources ? newsItem.articles : newsItem.articles.slice(0, 2);
  const hasMoreSources = newsItem.articles.length > 2;

  // Optional: Use the first article's image as the news item image
  const imageUrl = newsItem.articles[0]?.article_url || 'default_image_path_here';

  return (
    <Card sx={{ 
      width: '100%',
      my: 2,
      boxShadow: 3,
      display: 'flex',
      flexDirection: { xs: 'column', md: isRTL ? 'row-reverse' : 'row' },
      alignSelf: 'center',
      margin: 'auto',
      direction: isRTL ? 'rtl' : 'ltr',
      gap: 3
    }}>
      {/* Image Section */}
      <Box sx={{ 
        flex: '0 0 30%',
        maxWidth: '30%',
        height: 300,
        overflow: 'hidden',
        order: isRTL ? 2 : 0,
        marginRight: isRTL ? 0 : 2,
        marginLeft: isRTL ? 2 : 0
      }}>
        <CardMedia
          component="img"
          image={imageUrl}
          alt={newsItem.title}
          sx={{ 
            height: '100%', 
            width: '100%', 
            objectFit: 'cover'
          }}
        />
      </Box>

      {/* Content Section */}
      <Box sx={{ 
        flex: 1, 
        p: 3,
        minWidth: 0,
        maxWidth: '65%',
        flexShrink: 1,
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'space-between',
        textAlign: isRTL ? 'right' : 'left',
        alignSelf: 'center'
      }}>
        <Box>
          <Typography variant="h4" gutterBottom sx={{ 
            fontWeight: 'bold',
            textAlign: isRTL ? 'right' : 'left'
          }}>
            {newsItem.title}
          </Typography>

          {/* Expandable Content - now using summary */}
          <Typography paragraph sx={{ 
            textAlign: isRTL ? 'right' : 'left',
            overflow: 'hidden',
            display: '-webkit-box',
            WebkitLineClamp: expanded ? 'unset' : 3,
            WebkitBoxOrient: 'vertical',
            overflowWrap: 'break-word'
          }}>
            {expanded ? newsItem.summary : newsItem.summary.substring(0, 150) + '...'}
          </Typography>
          <Typography
            variant="body2"
            color="primary"
            onClick={() => setExpanded(!expanded)}
            sx={{ 
              cursor: 'pointer',
              display: 'block',
              textAlign: isRTL ? 'right' : 'left',
              mt: 1
            }}
          >
            {expanded ? (isRTL ? 'قراءة أقل' : 'Read LesS') : (isRTL ? 'قراءة المزيد' : 'Read More')}
          </Typography>
        </Box>

        {/* Sources Section */}
        <Box sx={{ flex: 1, p: 3, minWidth: 0, maxWidth: '35%' }}>
          <Typography variant="subtitle2" sx={{ color: 'text.secondary', mb: 1 }}>
            {isRTL ? 'المصادر:' : 'Sources:'}
          </Typography>
          {newsItem.articles.map((article, index) => (
            <Link
              key={index}
              href={article.article_url}
              target="_blank"
              rel="noopener noreferrer"
              sx={{ display: 'block', color: 'primary.main', '&:hover': { textDecoration: 'underline' } }}
            >
              {article.source_name}
            </Link>
          ))}
        </Box>
      </Box>
    </Card>
  );
};
