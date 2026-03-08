import axios from 'axios';
import type { Product, PricingAnalysis, CompetitorAnalysis, ChatMessage } from '../types';

const API_BASE_URL = import.meta.env.VITE_API_ENDPOINT || 'http://localhost:3000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getProducts = async (): Promise<{ count: number; products: Product[] }> => {
  const response = await api.get('/products');
  return response.data;
};

export const getProduct = async (id: string): Promise<Product> => {
  const response = await api.get(`/products/${id}`);
  return response.data;
};

export const getPricingAnalysis = async (productId: string): Promise<PricingAnalysis> => {
  const response = await api.post(`/analyze/pricing/${productId}`);
  return response.data;
};

export const getCompetitorAnalysis = async (productId: string): Promise<CompetitorAnalysis> => {
  const response = await api.post(`/analyze/competitors/${productId}`);
  return response.data;
};

export const sendChatMessage = async (
  message: string,
  conversationId: string = 'default',
  history: any[] = []
): Promise<ChatMessage> => {
  const response = await api.post('/chat', {
    message,
    conversation_id: conversationId,
    history,
  });
  return response.data;
};

export const healthCheck = async (): Promise<{ status: string }> => {
  const response = await api.get('/health');
  return response.data;
};
