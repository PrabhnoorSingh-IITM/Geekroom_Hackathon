import pytest
from pathlib import Path
from src.research_agent import filter_payloads, SourcePayload

def test_filter_payloads_sku():
    payloads = {
        "catalog": SourcePayload(name="catalog", records=[
            {"sku": "SKU1", "category": "Cat1"},
            {"sku": "SKU2", "category": "Cat1"},
            {"sku": "SKU3", "category": "Cat2"},
        ], loaded_from="inline"),
        "reviews": SourcePayload(name="reviews", records=[
            {"sku": "SKU1", "rating": 5},
            {"sku": "SKU2", "rating": 4},
            {"sku": "SKU3", "rating": 3},
        ], loaded_from="inline"),
        "pricing": SourcePayload(name="pricing", records=[], loaded_from="none"),
        "competitors": SourcePayload(name="competitors", records=[], loaded_from="none"),
        "performance_signals": SourcePayload(name="performance_signals", records=[], loaded_from="none"),
    }
    
    # Filter by SKU
    filtered = filter_payloads("SKU1", payloads)
    assert len(filtered["catalog"]) == 1
    assert filtered["catalog"][0]["sku"] == "SKU1"
    assert len(filtered["reviews"]) == 1
    assert filtered["reviews"][0]["sku"] == "SKU1"

def test_filter_payloads_category():
    payloads = {
        "catalog": SourcePayload(name="catalog", records=[
            {"sku": "SKU1", "category": "Cat1"},
            {"sku": "SKU2", "category": "Cat1"},
            {"sku": "SKU3", "category": "Cat2"},
        ], loaded_from="inline"),
        "reviews": SourcePayload(name="reviews", records=[
            {"sku": "SKU1", "rating": 5},
            {"sku": "SKU2", "rating": 4},
            {"sku": "SKU3", "rating": 3},
        ], loaded_from="inline"),
        "pricing": SourcePayload(name="pricing", records=[], loaded_from="none"),
        "competitors": SourcePayload(name="competitors", records=[], loaded_from="none"),
        "performance_signals": SourcePayload(name="performance_signals", records=[], loaded_from="none"),
    }
    
    # Filter by Category
    filtered = filter_payloads("Cat1", payloads)
    assert len(filtered["catalog"]) == 2
    skus = {r["sku"] for r in filtered["catalog"]}
    assert skus == {"SKU1", "SKU2"}
    assert len(filtered["reviews"]) == 2

def test_filter_payloads_empty():
    payloads = {
        "catalog": SourcePayload(name="catalog", records=[
            {"sku": "SKU1", "category": "Cat1"},
        ], loaded_from="inline"),
        "reviews": SourcePayload(name="reviews", records=[
            {"sku": "SKU1", "rating": 5},
        ], loaded_from="inline"),
        "pricing": SourcePayload(name="pricing", records=[], loaded_from="none"),
        "competitors": SourcePayload(name="competitors", records=[], loaded_from="none"),
        "performance_signals": SourcePayload(name="performance_signals", records=[], loaded_from="none"),
    }
    
    # Filter by empty string
    filtered = filter_payloads("", payloads)
    assert len(filtered["catalog"]) == 1
    assert len(filtered["reviews"]) == 1

def test_filter_payloads_no_match():
    payloads = {
        "catalog": SourcePayload(name="catalog", records=[
            {"sku": "SKU1", "category": "Cat1"},
        ], loaded_from="inline"),
        "reviews": SourcePayload(name="reviews", records=[
            {"sku": "SKU1", "rating": 5},
        ], loaded_from="inline"),
        "pricing": SourcePayload(name="pricing", records=[], loaded_from="none"),
        "competitors": SourcePayload(name="competitors", records=[], loaded_from="none"),
        "performance_signals": SourcePayload(name="performance_signals", records=[], loaded_from="none"),
    }
    
    # Filter by something that doesn't exist
    filtered = filter_payloads("NONEXISTENT", payloads)
    # Should fallback to original if no match (based on current implementation) 
    # OR it should return empty? The current impl returns all if no match.
    assert len(filtered["catalog"]) == 1 

if __name__ == "__main__":
    pytest.main([__file__])
