export class News {
  constructor(
    public id: string,
    public title: string,
    public summary: string,
    public publish_date: string,
    public articles: Array<{
      article_title: string;
      article_url: string;
      article_content: string;
      source_name: string;
      source_url: string;
    }>
  ) {}
}
