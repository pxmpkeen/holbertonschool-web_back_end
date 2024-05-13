// eslint-disable-next-line import/extensions, no-unused-vars
import Currency from './3-currency.js';

export default class Pricing {
  constructor(price, currency) {
    this._price = price;
    this._currency = currency;

    if (typeof this._price !== 'number') {
      throw new TypeError('price must be a number');
    }

    if (!(this._currency instanceof Currency)) {
      throw new TypeError('currency must be an instance of Currency');
    }
  }

  get price() {
    return this._price;
  }

  set price(value) {
    this._price = value;
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    this._currency = value;
  }

  displayFullPrice() {
    return `${this._price} ${this._currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
