export const CURRENCIES = {
  USD: { symbol: '$', rate: 1, name: 'US Dollar' },
  INR: { symbol: '₹', rate: 1, name: 'Indian Rupee' }, // Treat prices as already in INR
  EUR: { symbol: '€', rate: 0.92, name: 'Euro' },
  GBP: { symbol: '£', rate: 0.79, name: 'British Pound' },
};

export type CurrencyCode = keyof typeof CURRENCIES;

export const formatCurrency = (amount: number, currency: CurrencyCode = 'INR'): string => {
  const { symbol, rate } = CURRENCIES[currency];
  const convertedAmount = amount * rate;
  return `${symbol}${convertedAmount.toFixed(2)}`;
};

export const convertAmount = (amount: number, currency: CurrencyCode = 'INR'): number => {
  const { rate } = CURRENCIES[currency];
  return amount * rate;
};
