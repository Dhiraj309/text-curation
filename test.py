from datasets import Dataset
from text_curation import TextCurator

ds = Dataset.from_dict({
    "text": [
        # 1️⃣ Extreme whitespace + repetition + casing chaos
        """
        HELLO      world     world   WORLD!!!!
        
        
        this     is      a        test............
        this     is      a        test............
        this     is      a        test............
        """ ,

        # 2️⃣ Emails, phones, urls, tracking junk, repetition
        """
        Contact    me   at   TEST@Example.com   or test@example.com!!!
        Phone: +1 (415) 555-1234   /   415-555-1234
        Website: https://example.com?utm_source=spam&utm_campaign=spam
        Website: https://example.com?utm_source=spam&utm_campaign=spam
        """ ,

        # 3️⃣ Empty / near-empty / junk-only text
        "     \n\n\n     ",
        
        # 4️⃣ Unicode noise, emojis, broken punctuation
        """
        😃😃😃 THIS ——— is–––weird… text!!!
        Smart quotes “like this” and ‘this’.
        Non-breaking spaces and zero-width​chars.
        """ ,

        # 5️⃣ Fake structure: headers, bullets, broken lists
        """
        ### TITLE: SAMPLE DOCUMENT ###
        
        - item one
        - item two
        - item two
        - item two
        
        1) first point
        2) second point
        2) second point
        
        END END END
        """ ,

        # 6️⃣ PII + credentials + identifiers (for RedactBlock)
        """
        User: john_doe_1989
        Email: john.doe+test@gmail.com
        Backup email: john.doe@yahoo.com
        
        SSN: 123-45-6789
        Credit Card: 4111 1111 1111 1111
        IP Address: 192.168.1.42
        
        API_KEY=sk-test-1234567890abcdef
        """ ,

        # 7️⃣ Spammy boilerplate + legal junk
        """
        THIS MESSAGE IS CONFIDENTIAL.
        THIS MESSAGE IS CONFIDENTIAL.
        THIS MESSAGE IS CONFIDENTIAL.
        
        If you are not the intended recipient please delete this message.
        If you are not the intended recipient please delete this message.
        """ ,

        # 8️⃣ Long, rambling, redundant paragraph
        """
        This is a very very very long paragraph that keeps saying the same thing
        again and again and again because redundancy is extremely common in raw
        web text and scraped documents and documents that come from forums or
        user generated content where people tend to repeat themselves again
        and again and again for emphasis emphasis emphasis.
        """ ,
    ]
})

curator = TextCurator.from_profiles("web_common_v1")

out = ds.map(curator, batched=True)

for text in out["text"]:
    print(text, "\n\n\n")