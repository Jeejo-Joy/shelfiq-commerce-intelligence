export interface Product {
  product_id: string;
  name: string;
  category: string;
  current_price: number;
  cost: number;
  competitor_prices: number[];
  competitor_names: string[];
  sales_rank: number;
  rating: number;
  review_count: number;
  last_updated?: string;
}

export interface PricingAnalysis {
  product_id: string;
  timestamp: string;
  analysis_type: string;
  current_price: number;
  suggested_price: number;
  reasoning: string;
  competitive_position: string;
  expected_impact: string;
  confidence_score: number;
}

export interface CompetitorAnalysis {
  product_id: string;
  current_price: number;
  competitor_count: number;
  price_rank: number;
  percentile: number;
  competitive_position: string;
  min_competitor_price: number;
  max_competitor_price: number;
  median_competitor_price: number;
  recommended_action: string;
  competitors: Array<{
    name: string;
    price: number;
  }>;
}

export interface ChatMessage {
  conversation_id: string;
  message: string;
  timestamp: string;
}
