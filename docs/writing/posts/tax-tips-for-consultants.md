---
date: 2024-12-18
authors:
- nirant
categories:
- niranting
title: Tax Tips for Technical Consultants in India
---

Managing taxation and financial compliance as a consultant in India involves several considerations: GST to the benefits of Section 44ADA and the complexities of foreign entity considerations, consultants must juggle multiple aspects to ensure compliance and tax optimization. I'm sharing what I know in the hopes it's helpful to others.


## 1. Compliance: GST, LUT and FIRC

- **Threshold**: Acquiring a GST number becomes almost mandatory once your income surpasses some X=20 lakhs INR in a given financial year. This step legitimizes your income and ensures compliance with Indian taxation laws. The X limits keeps changing and I'd recommend you check the latest one with a CA and NOT rely on Google for this. Some online services like ClearTax offer GST registration services, but I'd recommend you get it done via a CA. It's a one-time process and you don't need to renew it every year.

- **Sole Proprietorship**: If you are an individual, you get a GST number as a sole proprietor. This is the simplest way to get a GST number and is recommended for most consultants. You can also get a GST number as a private limited company, but that might be overkill for most consultants. My CA also recommended that I get an Udyog Certificate, so I did get one but I'm not sure if it's necessary.
  
- **Quarterly Filing**: If you are a sole proprietor or operating as an individual consultant, quarterly GST filing can be more manageable than doing it monthly. This approach helps streamline administrative tasks and keeps compliance straightforward.

- **FIRC**: Every time that you receive a payment from a foreign entity, you will need to get a Foreign Inward Remittance Certificate (FIRC) from your bank. This document is a proof of payment and is required for filing taxes. It is advisable to get a FIRC for each payment, as it can be difficult to get one later. [Salt](https://www.salt.pe/) is a great tool for automating this process.

- **Accounting & Compliance**: Using a CA to file for managing both your GST and Letter of Undertaking (LUT) is advisable. It serves as an effective tool for official documentation and ensures a smoother filing process.
  
- **Current Account**: Having a current account separate from your personal finances helps in meticulous financial management. It allows you to distinctly separate your business income and expenses, making accounting more cleaner. E.g. you can use this current to pay for your AWS bills. This can help you save on GST, as you can claim GST input credit on these expenses.

- **Letter of Undertaking (LUT)**: For consultants involved in international transactions, an LUT is crucial. This legal document clarifies that all relevant taxes will be paid exclusively in India, thereby simplifying compliance requirements for cross-border business. It is advisable to get an LUT even if you are not sure if you will be involved in international transactions. You need to mention the LUT in your invoices to foreign entities.

- **GST on Foreign Transactions**: GST is not applicable on foreign transactions. However, you will need to mention the LUT in your invoices to foreign entities. This is to ensure that the GST authorities are aware that you are not liable to pay GST on these transactions.


### 1.1 GST Filing
- **GST Filing**: You can file GST monthly or quarterly. I'd recommend you to file quarterly, as it's easier to manage. I also recommend hiring a CA to do this for you who can also help you with other compliances.

### 1.2 Address
- I'd recommend you to get a separate address for your business. I use a Virtual Office address and that works. I'd recommend that you get this somewhere you can visit if needed by the bank or tax authorities.
- If you are a consultant, you can use your home address as your business address. This will need a NoC from the title owner of the property. This owner might be your landlord or your parents.
- GST Number is different for each state/billing address


## 2. Taxation

### 2.1 Personal Income Tax: Section 44ADA

- **50% Rule**: Section 44ADA offers a benefit by allowing you to assume 50% of your income upto 75 lakhs as an expense for tax filing. This helps significantly in reducing your taxable income, which can be advantageous for many consultants. 


Example Math:

If you make 72 lakhs INR in a year, you can assume 36 lakhs INR (half of 75 lakhs) as your expenses and pay taxes on the remaining 72-36=36 lakhs INR. At 30% income tax rate, you'd pay 10.8 lakhs INR in taxes. Effectively, you'd be paying 10.8/72 = 15% of your income in taxes.

💡 You do NOT need to maintain books of expenses for Section 44ADA. This is a huge benefit as it simplifies the process of filing taxes!

There is another catch on 100 lakhs INR: 15% surcharge on income tax. Source: [ClearTax](https://cleartax.in/s/marginal-relief-surcharge) -- I'm unclear if Section 44ADA applies to this surcharge. 

- **>50% Expenses**: If your actual expenses amount to more than half of your income, then Section 44ADA may not offer you the best tax advantage. This is because you can only claim 50% of your income as an expense, even if your actual expenses are higher. You will have to get audited by a CA and file your taxes later (usually in September) if you want to claim more than 50% of your income as expenses.

### 2.2 Foreign LLC or C-Corp

- **LLC Abroad**: If you are working with a foreign entity, it is sometimes useful to have a Limited Liability Company (LLC) in the country of the entity. E.g. you can open a Delaware LLC via [Stripe Atlas](https://stripe.com/atlas) and use that to invoice your clients. You will then pay taxes via this entity in the source country. It's only for the amount that you move to India, that you will pay taxes in India. 

If I remember correctly, you will be paying 8.7% _corporate tax_ in Delaware, and similarly 8-9% in Dubai. With all of these, you pay additional 30% _personal income tax_ in India. So if you make 100 lakhs INR in a year, you will pay 8.7 lakhs INR in the US. And then you pay personal income tax in India on your living expenses: So say, you move 18 lakhs INR to India, you will pay 0.3*18 = 5.4 lakhs INR in taxes in India. Effectively, you'd be paying 14.1% of your income in taxes. If you are making more than 100 lakhs INR in a year, this might be a good option for you.

This can help simplify the process of receiving payments. However, it is important to note that this option is not always the most tax-efficient. It is advisable to consult a CA to understand the implications of this option for your specific amount, transaction frequency and expected personal expenses.

RemoteIndian has a similar [Tax Guide](https://remoteindian.com/guides/tax-guide) that you might find useful. 


## 3. Invoicing

I use [Refrens](https://refrens.com) to invoice my clients. It's a great tool for invoicing and managing your invoices. Here are some of the fields which I'd recommend you to fill in: 

1. **GSTIN**: This is your GST number.
2. **Billed To**: This is the name, address, phone number, PAN and GSTIN of the client.
3. **Invoice Date**: This is the date of the invoice.
4. **Due Date**: This is the date by which the client needs to pay the invoice.
5. **Invoice Number**: This is the invoice number.
6. **Invoice Amount**: This is the amount of the invoice.
7. **Invoice Currency**: This is the currency of the invoice.


I'm not a CA, so please consult a CA before making any decisions. I'm sharing what I know in the hopes it's helpful to others. If you have any questions, please feel free to reach out to me on [Twitter](https://twitter.com/nirantk).