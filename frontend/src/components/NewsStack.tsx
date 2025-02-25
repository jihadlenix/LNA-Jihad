import { useState, useEffect } from 'react';
import axios from 'axios';
import Box from '@mui/material/Box';
import NewsCard from './NewsCard';

// Define the structure for each article in the news story
interface Article {
  article_title: string;
  article_url: string;
  article_content: string;
  source_name: string;
  source_url: string;
}

// Define the structure of a news item
class News {
  id: string;
  title: string;
  summary: string;
  publish_date: string;
  articles: Article[];

  constructor(id: string, title: string, summary: string, publish_date: string, articles: Article[]) {
    this.id = id;
    this.title = title;
    this.summary = summary;
    this.publish_date = publish_date;
    this.articles = articles;
  }
}

// Explicitly define the type for props
interface NewsStackProps {
  language: 'en' | 'ar';
}

const NewsStack = ({ language }: NewsStackProps) => {
  const [newsItems, setNewsItems] = useState<News[]>([]);  // Use generic to define state type

  useEffect(() => {
    axios.get('https://lebna-e8dhd0h3cfdyfwaz.uaenorth-01.azurewebsites.net/news/aggregated-stories/')
      .then(response => {
        // Transform API data to News instances if needed
        setNewsItems(response.data.map((item: any) => new News(
          item.id,
          item.title,
          item.summary,
          item.publish_date,
          item.articles
        )));
      })
      .catch(error => console.error('Fetching news failed:', error));
  }, [language]);  // Refetch when language changes if your API supports language queries

  return (
    <Box sx={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      width: '100%',
      padding: 3
    }}>
      {newsItems.map((item, index) => (
        <NewsCard key={index} newsItem={item} language={language} />
      ))}
    </Box>
  );
};

export default NewsStack;
