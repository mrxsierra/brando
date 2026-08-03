"""
Brando Feature Module 6D: Trademark & Legal Vetting Engine (Section 6.D of PRD v2)
Maps Nice International Trademark Classes (1-45) and simulates WIPO Madrid Protocol clearance.
"""

from typing import Dict, Any, List, Set


NICE_CLASSES_MAP: Dict[int, str] = {
    9: "Computer Software, Electronics & Scientific Instruments",
    35: "Advertising, Business Management & Commercial Services",
    36: "Financial, Banking, Real Estate & Insurance Services",
    38: "Telecommunications, Messaging & Digital Communication",
    42: "Software-as-a-Service (SaaS), Technology Services & Cloud Computing",
    45: "Legal, Security & Domain Identity Services",
}


class TrademarkModule:
    """
    Module 6D: Trademark & Nice Class Vetting Engine.
    """

    @staticmethod
    def map_nice_classes(requested_classes: List[int]) -> Dict[int, str]:
        """
        Maps requested Nice Class numbers to international class descriptions.
        """
        result: Dict[int, str] = {}
        for cls_num in requested_classes:
            result[cls_num] = NICE_CLASSES_MAP.get(cls_num, f"Nice Class {cls_num} General")
        return result

    @classmethod
    def audit_trademark_clearance(cls, candidate: str, target_classes: List[int]) -> Dict[str, Any]:
        """
        Simulates WIPO Madrid Protocol and regional trademark clearance audit.
        """
        text = candidate.lower()
        mapped_classes = cls.map_nice_classes(target_classes)

        # Risk heuristics based on common/famous brand clashes
        risk_score = 10 # Baseline low risk score
        clearance_warnings: List[str] = []

        if len(text) <= 4:
            risk_score += 20
            clearance_warnings.append("short_name_clash_risk")

        if any(cls_num in [9, 42] for cls_num in target_classes):
            if "tech" in text or "soft" in text:
                risk_score += 15
                clearance_warnings.append("descriptive_tech_term")

        clearance_status = "CLEARED" if risk_score < 40 else "REVIEW_REQUIRED"

        return {
            "candidate": candidate,
            "target_classes": target_classes,
            "mapped_classes": mapped_classes,
            "risk_score": risk_score,
            "clearance_status": clearance_status,
            "clearance_warnings": clearance_warnings,
        }
