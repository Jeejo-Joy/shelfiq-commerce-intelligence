import { useState, useEffect } from 'react';
import { getProducts, getProduct, getPricingAnalysis, getCompetitorAnalysis } from './services/api';
import type { Product, PricingAnalysis, CompetitorAnalysis } from './types';
import { formatCurrency, type CurrencyCode } from './utils/currency';
import './App.css';

function App() {
  const [products, setProducts] = useState<Product[]>([]);
  const [selectedProduct, setSelectedProduct] = useState<Product | null>(null);
  const [pricingAnalysis, setPricingAnalysis] = useState<PricingAnalysis | null>(null);
  const [competitorAnalysis, setCompetitorAnalysis] = useState<CompetitorAnalysis | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [view, setView] = useState<'list' | 'detail'>('list');
  const [currency] = useState<CurrencyCode>('INR'); // Default to Indian Rupees

  useEffect(() => {
    loadProducts();
  }, []);

  const loadProducts = async () => {
    try {
      setLoading(true);
      const data = await getProducts();
      setProducts(data.products);
      setError(null);
    } catch (err) {
      setError('Failed to load products');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleProductClick = async (productId: string) => {
    try {
      setLoading(true);
      const product = await getProduct(productId);
      setSelectedProduct(product);
      setView('detail');

      // Load analyses
      const [pricing, competitor] = await Promise.all([
        getPricingAnalysis(productId).catch(() => null),
        getCompetitorAnalysis(productId).catch(() => null),
      ]);

      setPricingAnalysis(pricing);
      setCompetitorAnalysis(competitor);
      setError(null);
    } catch (err) {
      setError('Failed to load product details');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleBackToList = () => {
    setView('list');
    setSelectedProduct(null);
    setPricingAnalysis(null);
    setCompetitorAnalysis(null);
  };

  return (
    <div className="app">
      <header className="app-header">
        <h1>🛒 ShelfIQ - AI Commerce Intelligence</h1>
        <p>Powered by Amazon Bedrock & AWS</p>
      </header>

      {error && (
        <div className="error-banner">
          ⚠️ {error}
        </div>
      )}

      {loading && <div className="loading">Loading...</div>}

      {view === 'list' && (
        <div className="product-list-view">
          <div className="stats-bar">
            <div className="stat-card">
              <h3>{products.length}</h3>
              <p>Total Products</p>
            </div>
            <div className="stat-card">
              <h3>{new Set(products.map(p => p.category)).size}</h3>
              <p>Categories</p>
            </div>
            <div className="stat-card">
              <h3>{formatCurrency(products.reduce((sum, p) => sum + p.current_price, 0) / products.length || 0, currency)}</h3>
              <p>Avg Price</p>
            </div>
          </div>

          <div className="product-grid">
            {products.map((product) => (
              <div
                key={product.product_id}
                className="product-card"
                onClick={() => handleProductClick(product.product_id)}
              >
                <div className="product-category">{product.category}</div>
                <h3>{product.name}</h3>
                <div className="product-price">{formatCurrency(product.current_price, currency)}</div>
                <div className="product-meta">
                  <span>⭐ {product.rating.toFixed(1)}</span>
                  <span>📊 Rank: {product.sales_rank}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {view === 'detail' && selectedProduct && (
        <div className="product-detail-view">
          <button className="back-button" onClick={handleBackToList}>
            ← Back to Products
          </button>

          <div className="detail-header">
            <h2>{selectedProduct.name}</h2>
            <span className="category-badge">{selectedProduct.category}</span>
          </div>

          <div className="detail-grid">
            <div className="detail-card">
              <h3>Product Information</h3>
              <div className="info-row">
                <span>Current Price:</span>
                <strong>{formatCurrency(selectedProduct.current_price, currency)}</strong>
              </div>
              <div className="info-row">
                <span>Cost:</span>
                <strong>{formatCurrency(selectedProduct.cost, currency)}</strong>
              </div>
              <div className="info-row">
                <span>Margin:</span>
                <strong>{(((selectedProduct.current_price - selectedProduct.cost) / selectedProduct.current_price) * 100).toFixed(1)}%</strong>
              </div>
              <div className="info-row">
                <span>Sales Rank:</span>
                <strong>{selectedProduct.sales_rank}</strong>
              </div>
              <div className="info-row">
                <span>Rating:</span>
                <strong>⭐ {selectedProduct.rating.toFixed(1)} ({selectedProduct.review_count} reviews)</strong>
              </div>
            </div>

            {pricingAnalysis && (
              <div className="detail-card pricing-card">
                <h3>💡 AI Pricing Recommendation</h3>
                <div className="suggested-price">
                  Suggested: {formatCurrency(Number(pricingAnalysis.suggested_price || 0), currency)}
                </div>
                <div className="confidence">
                  Confidence: {(Number(pricingAnalysis.confidence_score || 0) * 100).toFixed(0)}%
                </div>
                <div className="reasoning">
                  <strong>Reasoning:</strong>
                  <p>{pricingAnalysis.reasoning}</p>
                </div>
                <div className="position-badge">
                  Position: {pricingAnalysis.competitive_position}
                </div>
              </div>
            )}

            {competitorAnalysis && (
              <div className="detail-card competitor-card">
                <h3>🎯 Competitor Analysis</h3>
                <div className="competitor-stats">
                  <div className="stat">
                    <span>Market Position:</span>
                    <strong>{competitorAnalysis.competitive_position}</strong>
                  </div>
                  <div className="stat">
                    <span>Price Rank:</span>
                    <strong>{competitorAnalysis.price_rank} of {competitorAnalysis.competitor_count + 1}</strong>
                  </div>
                  <div className="stat">
                    <span>Percentile:</span>
                    <strong>{Number(competitorAnalysis.percentile).toFixed(1)}%</strong>
                  </div>
                </div>
                <div className="price-range">
                  <div>Min: {formatCurrency(Number(competitorAnalysis.min_competitor_price), currency)}</div>
                  <div>Median: {formatCurrency(Number(competitorAnalysis.median_competitor_price), currency)}</div>
                  <div>Max: {formatCurrency(Number(competitorAnalysis.max_competitor_price), currency)}</div>
                </div>
                <div className="action-box">
                  <strong>Recommended Action:</strong>
                  <p>{competitorAnalysis.recommended_action}</p>
                </div>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
